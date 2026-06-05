# pages/3_Quiz.py

import streamlit as st
import re

from utils.ai_client import generate_quiz
from utils.supabase_client import save_quiz_result
from components.styles import (
    load_css,
    hero_section,
    footer
)

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="AI Quiz | ExamPrep AI",
    page_icon="📝",
    layout="wide"
)

load_css()

# --------------------------------------------------
# AUTH CHECK
# --------------------------------------------------

if not st.session_state.get("authenticated", False):
    st.warning("Please login first.")
    st.stop()

user = st.session_state.get("user")

if not user:
    st.error("User session not found.")
    st.stop()

# --------------------------------------------------
# HEADER
# --------------------------------------------------

hero_section(
    "📝 AI Quiz Generator",
    "Generate and practice personalized quizzes."
)

# --------------------------------------------------
# QUIZ SETTINGS
# --------------------------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    exam = st.selectbox(
        "Exam",
        [
            "JEE",
            "NEET",
            "UPSC",
            "CAT",
            "GATE",
            "SSC",
            "Banking",
            "General"
        ]
    )

with col2:
    subject = st.text_input(
        "Subject",
        placeholder="Physics"
    )

with col3:
    topic = st.text_input(
        "Topic",
        placeholder="Newton Laws"
    )

num_questions = st.slider(
    "Number of Questions",
    5,
    20,
    10
)

# --------------------------------------------------
# GENERATE QUIZ
# --------------------------------------------------

if st.button("Generate Quiz"):

    if not subject or not topic:
        st.error("Please enter subject and topic.")
        st.stop()

    with st.spinner("Generating quiz..."):

        quiz_text = generate_quiz(
            exam=exam,
            subject=subject,
            topic=topic,
            num_questions=num_questions
        )

        st.session_state.quiz_text = quiz_text

# --------------------------------------------------
# DISPLAY QUIZ
# --------------------------------------------------

if "quiz_text" in st.session_state:

    st.subheader("Generated Quiz")

    st.text_area(
        "Quiz",
        st.session_state.quiz_text,
        height=500
    )

# --------------------------------------------------
# SIMPLE SCORE ENTRY
# --------------------------------------------------

st.markdown("---")

st.subheader("Save Quiz Result")

score = st.number_input(
    "Score Obtained",
    min_value=0,
    value=0
)

total = st.number_input(
    "Total Marks",
    min_value=1,
    value=10
)

time_taken = st.number_input(
    "Time Taken (minutes)",
    min_value=0,
    value=0
)

if st.button("Save Result"):

    try:

        save_quiz_result(
            user_id=user.id,
            subject=subject if subject else "General",
            topic=topic if topic else "General",
            score=score,
            total=total,
            time_taken=time_taken
        )

        st.success(
            "Quiz result saved successfully."
        )

    except Exception as e:

        st.error(str(e))

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

footer()