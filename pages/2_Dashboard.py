# pages/2_Dashboard.py

import streamlit as st
import pandas as pd

from utils.supabase_client import (
    get_profile,
    get_quiz_results
)

from utils.ai_client import (
    get_motivation,
    analyze_performance
)

from components.styles import (
    load_css,
    hero_section,
    footer
)

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Dashboard | ExamPrep AI",
    page_icon="📊",
    layout="wide"
)

load_css()

# --------------------------------------------------
# AUTH CHECK
# --------------------------------------------------

if not st.session_state.get("authenticated", False):
    st.warning("Please login first.")
    st.stop()

# --------------------------------------------------
# USER INFO
# --------------------------------------------------

user = st.session_state.get("user")

if not user:
    st.error("User session not found.")
    st.stop()

user_id = user.id

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

profile = get_profile(user_id)
quiz_results = get_quiz_results(user_id)

# --------------------------------------------------
# HERO
# --------------------------------------------------

user_name = "Student"

if profile and profile.get("name"):
    user_name = profile["name"]

hero_section(
    f"🎓 Welcome, {user_name}",
    "Track your progress and study smarter with AI."
)

# --------------------------------------------------
# PROFILE CARD
# --------------------------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.info(
        f"🎯 Exam: {profile.get('exam_type', 'General') if profile else 'General'}"
    )

with col2:
    st.info(
        f"⏰ Daily Study Hours: {profile.get('daily_hours', 4) if profile else 4}"
    )

with col3:
    st.info(
        f"📧 {profile.get('email', '') if profile else ''}"
    )

# --------------------------------------------------
# QUIZ STATS
# --------------------------------------------------

total_quizzes = len(quiz_results)

avg_score = 0

if quiz_results:
    percentages = [
        float(item.get("percentage", 0))
        for item in quiz_results
    ]

    avg_score = round(
        sum(percentages) / len(percentages),
        2
    )

best_score = 0

if quiz_results:
    best_score = max(
        float(item.get("percentage", 0))
        for item in quiz_results
    )

# --------------------------------------------------
# METRICS
# --------------------------------------------------

st.subheader("📈 Performance Overview")

m1, m2, m3 = st.columns(3)

with m1:
    st.metric(
        "Total Quizzes",
        total_quizzes
    )

with m2:
    st.metric(
        "Average Score",
        f"{avg_score}%"
    )

with m3:
    st.metric(
        "Best Score",
        f"{best_score}%"
    )

# --------------------------------------------------
# DAILY MOTIVATION
# --------------------------------------------------

st.subheader("🔥 Daily Motivation")

try:

    motivation = get_motivation(
        profile.get("exam_type", "General")
        if profile else "General"
    )

    st.success(motivation)

except Exception:
    st.info(
        "Stay consistent. Small progress every day creates big success."
    )

# --------------------------------------------------
# RECENT QUIZZES
# --------------------------------------------------

st.subheader("📝 Recent Quiz Attempts")

if quiz_results:

    df = pd.DataFrame(quiz_results)

    columns_to_show = [
        col for col in [
            "subject",
            "topic",
            "score",
            "total",
            "percentage",
            "created_at"
        ]
        if col in df.columns
    ]

    st.dataframe(
        df[columns_to_show],
        use_container_width=True
    )

else:

    st.info(
        "No quiz attempts found."
    )

# --------------------------------------------------
# AI ANALYSIS
# --------------------------------------------------

st.subheader("🤖 AI Performance Insights")

if quiz_results:

    try:

        latest_results = quiz_results[:10]

        analysis = analyze_performance(
            str(latest_results)
        )

        st.markdown(analysis)

    except Exception as e:

        st.warning(
            f"AI analysis unavailable: {e}"
        )

else:

    st.info(
        "Take a few quizzes to unlock AI insights."
    )

# --------------------------------------------------
# WEAK TOPICS
# --------------------------------------------------

st.subheader("📚 Improvement Suggestions")

if quiz_results:

    weak_topics = []

    for item in quiz_results:

        percentage = float(
            item.get("percentage", 0)
        )

        if percentage < 60:
            weak_topics.append(
                item.get("topic", "Unknown")
            )

    weak_topics = list(set(weak_topics))

    if weak_topics:

        st.warning(
            "Topics needing attention:"
        )

        for topic in weak_topics:
            st.write(f"• {topic}")

    else:

        st.success(
            "Great job! No major weak topics detected."
        )

else:

    st.info(
        "Complete quizzes to discover weak topics."
    )

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

footer()