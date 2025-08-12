from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from dotenv import load_dotenv
import os
from google.genai import Client
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import secrets
from pathlib import Path


app = Flask(__name__)

load_dotenv()

limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)
limiter.init_app(app)

app.secret_key = os.getenv("FLASK_SECRET_KEY")
API_KEY = os.getenv("GOOGLE_API_KEY")

if not app.secret_key:
    raise RuntimeError("FLASK_SECRET_KEY is not set in environment")

if not API_KEY:
    raise RuntimeError("GOOGLE_API_KEY is not set in environment")


client = Client(api_key=API_KEY)

class CodeFarm:
    @staticmethod
    def challenge(level, language):
        prompt = f"""
        Create a coding challenge for a {level} level who learn {language}.
        
        Use farming metaphors and keep it appropriate for their level. Format:
        
        **🌱 Challenge:** [Title with farming theme]
        **📝 Task:** [What they need to code]
        **🎯 Goal:** [Expected output]
        **💡 Hint:** [One helpful hint]
        **🌾 Example:** [Small example if helpful]
        
        Make it fun! Adjust difficulty for {level} level.
        """
        try:
            response = client.models.generate_content(
                model='gemini-2.0-flash-exp',
                contents=prompt
            )
            return response.text
        except Exception as e:
            print(f"Error generating challenge: {e}")
            return "Error growing challenge. Try again!"
    
    @staticmethod
    def inspect_code(code, challenge_desc=""):
        prompt = f"""
        You're a coach reviewing this code. Use farming language and be direct.
        
        Challenge context: {challenge_desc}
        
        Code Harvest:
        ```
        {code}
        ```
        Give feedback like:
        **🌟 What grew well:**
        [List positive aspects]
        
        **🌱 What needs more water:**
        [Suggestions for improvement]
        
        **🚜 Farming tip:**
        [One key learning point or best practice]
        
        **⭐ Harvest rating:** [1-5 stars] - [Brief explanation]
        
        **🎯 Next crop to plant:** [Suggestion for what to learn/practice next]
        
        Keep it encouraging and use farming metaphors throughout!
        """
        try:
            response = client.models.generate_content(
                model='gemini-2.0-flash-exp',
                contents=prompt
            )
            return response.text
        except Exception as e:
            print(f"Error inspecting harvest: {e}")
            return "Error inspecting harvest. Try again!"
    
 
def init_session():
    if 'farmer' not in session:
        session['farmer'] = {
            'level': 'seedling',
            'language': 'python'
        }

@app.route('/', methods=['GET', 'POST'])
@limiter.limit("5 per minute")
def home():
    if request.method == 'POST':
        if 'code' in request.form:
            code = request.form['code']
            challenge_desc = request.form.get('challenge_desc', '')
            review = CodeFarm.inspect_code(code, challenge_desc)
            return render_template('review.html', review=review)
    
    return render_template('home.html')

@app.route('/challenge', methods=['GET', 'POST'])
@limiter.limit("5 per minute")
def challenge():
    init_session()
    
    if request.method == 'POST':
        level = request.form['level']
        language = request.form['language']
        
        
        session['farmer']['level'] = level
        session['farmer']['language'] = language
        session.modified = True
        
   
        challenge = CodeFarm.challenge(level, language)

        farmer = session['farmer']
        return render_template('show_challenge.html', 
                             challenge=challenge,
                             level=farmer['level'],
                             language=farmer['language'])
    return render_template('challenge.html')

@app.route('/review', methods=['GET', 'POST'])
@limiter.limit("5 per minute")
def review():
    init_session()
    
    if request.method == 'POST':
        code = request.form['code']
        challenge_desc = request.form.get('challenge_desc', '')
        
        review = CodeFarm.inspect_code(code, challenge_desc)
        return render_template('review.html', review=review)
    
    return render_template('submit.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv("PORT", 5008)))
