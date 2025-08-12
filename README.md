# 🚜 Code Farm Academy

### AI Code Coach with Pixel Farm Vibes

A charming farming-themed code coaching app inspired by **Stardew Valley**! Built with Flask and Google's Generative AI, where coding feels like tending a digital farm. 🌾

![Farmer Level](https://img.shields.io/badge/Farmer%20Level-Seedling%20to%20Tree-4CAF50)
![Crops](https://img.shields.io/badge/Crops-Python%20|%20JavaScript%20|%20Java%20|%20More-FF8C00)
![Status](https://img.shields.io/badge/Status-Growing%20Strong-87CEEB)

---

## 🌱 **What This Farm Grows**

**Code Farm Academy** uses Google's Generative AI to help you cultivate your programming skills:

- **🌱 Generate Challenges** - Get coding problems tailored to your farmer level and preferred crop (language)
- **🔍 Review Harvests** - Submit your code solutions for wise old farmer feedback
- **📚 Farm Wisdom** - Learn programming concepts through delightful farming metaphors
- **🎮 Pixel Vibes** - Enjoy Stardew Valley-inspired animations.

_Perfect for anyone who like a cozy farming adventure!_

---

## 🎯 **Inspiration & Purpose**

- This project was born from a love of **Stardew Valley** and the desire to make coding fun.
- **This is purely a fun project** - no commercial intent 🌻

---

## 🔧 **Prerequisites**

- **Python**: 3.10+ recommended
- **Google AI API key**: Create one in [Google AI Studio](https://makersuite.google.com/app/apikey)
- **A love for farming games** (optional but recommended) 🐔

---

## 🏠 **How to Use Your Farm**

### **🏠 Farmhouse (`/`)**

- Quick actions and code review forms
- Generate instant challenges
- Submit code for expert farmer wisdom

### **🌱 Plant Challenges (`/challenge`)**

- Choose your **farmer level**: `seedling` (beginner), `sprout` (intermediate), `tree` (advanced)
- Pick your **crop type**: Python Snake Beans, JavaScript Lightning Lettuce, Java Coffee Beans, and more!
- Get a custom coding challenge that grows with your skills

### **🔍 Harvest Review (`/review`)**

- Submit your code solution (with optional challenge context)
- Receive encouraging feedback from our wise AI farmer
- Learn what grew well and what needs more water

### **🎮 Farm Atmosphere**

- **Walking Stardew Valley chicken** that pecks around the farm
- **Animated butterflies** fluttering across the screen
- **Drifting pixel clouds** in the sky
- **Grass footer** with that classic pixel art feel

---

## ⚙️ **Farm Configuration**

- **API Key**: Set in `.env` as `GOOGLE_API_KEY`
- **Session Secret**: Replace placeholder in `app.py` for production
- **AI Model**: Uses `gemini-2.0-flash-exp` by default

Example AI call:

```python
response = client.models.generate_content(
    model='gemini-2.0-flash-exp',
    contents=prompt
)
harvest_wisdom = response.text
```

---

## 📁 **Farm Layout**

```
code-farm-academy/
├── 🏠 app.py                 # Main farmhouse (Flask app + AI farmers)
├── 🌾 templates/             # Farm buildings (Jinja templates)
│   ├── base.html            # Foundation with animations
│   ├── home.html            # Farmhouse entrance
│   ├── challenge.html       # Seed selection
│   ├── show_challenge.html  # Growing field
│   └── review.html          # Harvest evaluation
├── 🎨 static/               # Farm decorations
│   ├── css/style.css       # Pixel art styling
│   └── images/             # Sprites and animations
│       ├── chicken.gif     # Stardew Valley chicken
│       ├── butterfly.gif   # Flutter animations
│       └── cloud.gif       # Sky decorations
└── 📜 requirements.txt      # Farming supplies list
```

---

### **🤖 AI-Powered Learning**

- **Personalized challenges** that grow with your skills
- **Encouraging feedback** that focuses on growth, not criticism
- **Farming language** that makes programming concepts approachable
- **Context-aware reviews** that understand what you were trying to solve

---

## 🎊 **Special Thanks**

- **ConcernedApe** for creating Stardew Valley and inspiring peaceful, nurturing digital experiences
- **Google** for making AI accessible to small farm projects

---

**Happy farming, and may your code grow strong! 🌾✨**

![stardew](https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExM2J4bmFydGtscnVobWUyejlmZHA4dnI2eXl5am1hOGR4NGtlNjhlayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/URExNvlgfjZ2rd5Gl0/giphy.gif)
