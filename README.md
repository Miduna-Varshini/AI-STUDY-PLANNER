# 🎓 ExamPrep AI — Personalised Study Intelligence

[![Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://examprep-ai7.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)](https://python.org)
[![Supabase](https://img.shields.io/badge/Supabase-PostgreSQL-3ECF8E?logo=supabase&logoColor=white)](https://supabase.com)

> An AI-powered learning platform built for competitive exam aspirants — JEE, NEET, UPSC, CAT, and GATE.

🚀 **Live App → [examprep-ai7.streamlit.app](https://examprep-ai7.streamlit.app/)**

---

## 📌 Overview

ExamPrep AI is a smart study companion that helps students prepare for India's most competitive exams. It combines AI-generated quizzes, personalised study plans, performance analytics, and an AI mentor — all in one platform.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🧠 **AI Quiz Generator** | Topic-wise quizzes with adjustable difficulty and real-time scoring |
| 📊 **Performance Analytics** | Track accuracy over time with subject-wise insights |
| 📅 **Smart Study Planner** | Personalised schedules based on exam type and daily study hours |
| 🤖 **AI Mentor** | Chat-based tutor for doubt solving, concept explanations, and motivation |
| 🎥 **Learning Videos** | YouTube-integrated topic-based video recommendations |
| 👤 **User Profile System** | Exam selection, daily goal setting, and personalised experience |

---

## 🏗️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend | [Streamlit](https://streamlit.io) |
| Backend | Python 3.10+ |
| Database & Auth | [Supabase](https://supabase.com) (PostgreSQL) |
| AI Models | [Groq](https://console.groq.com) / [OpenRouter](https://openrouter.ai) |
| Video API | [YouTube Data API v3](https://console.cloud.google.com) |
| Deployment | [Streamlit Cloud](https://share.streamlit.io) |

---

## 📁 Project Structure

```
examprep_ai/
├── app.py                  # Main entry point
├── pages/
│   ├── 1_Login.py
│   ├── 2_Dashboard.py
│   ├── 3_Quiz.py
│   ├── 4_Analytics.py
│   ├── 5_Study_Plan.py
│   ├── 6_Videos.py
│   ├── 7_AI_Mentor.py
│   └── 8_Profile.py
├── utils/
│   ├── supabase_client.py  # Supabase connection
│   ├── ai_client.py        # Groq / OpenRouter integration
│   ├── youtube_client.py   # YouTube API
│   └── helpers.py
├── components/
│   └── styles.py
├── requirements.txt
├── supabase_schema.sql     # Run this in Supabase SQL Editor
└── .env.example            # Environment variable template
```

---

## ⚙️ Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/examprep-ai.git
cd examprep-ai
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the root directory:

```env
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_anon_key
GROQ_API_KEY=your_groq_api_key
OPENROUTER_API_KEY=your_openrouter_api_key
YOUTUBE_API_KEY=your_youtube_api_key
```

### 5. Set up the database

1. Go to [supabase.com](https://supabase.com) and create a new project
2. Open the **SQL Editor**
3. Paste and run the contents of `supabase_schema.sql`

This creates the following tables:
- `profiles` — user details and exam selection
- `quiz_results` — quiz scores and history
- `study_plans` — personalised schedules
- `bookmarks` — saved videos and resources
- `chat_history` — AI mentor conversation logs

### 6. Run the app

```bash
streamlit run app.py
```

---

## 🔑 API Keys

| Service | Get your key |
|---|---|
| Supabase | [supabase.com](https://supabase.com) |
| Groq | [console.groq.com](https://console.groq.com) |
| OpenRouter | [openrouter.ai](https://openrouter.ai) |
| YouTube Data API | [console.cloud.google.com](https://console.cloud.google.com) |

---

## 🚀 Deployment (Streamlit Cloud)

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io) and connect your repo
3. Set `app.py` as the entry point
4. Add your environment variables under **App Settings → Secrets**

---

## 🎯 Roadmap

- [ ] PDF report generation
- [ ] Flashcard system with spaced repetition
- [ ] Leaderboard and gamification
- [ ] Mobile app version
- [ ] Daily reminders and push notifications
- [ ] Voice-based AI mentor

---

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m 'Add your feature'`
4. Push and open a Pull Request

---

## 👨‍💻 Author

**Miduna Varshini M A**

---

⭐ If this project helped you, give it a star on GitHub and share it with fellow aspirants!
