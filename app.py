# app.py

import streamlit as st
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="🎓 ExamPrep AI",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# CUSTOM CSS
# -----------------------------
st.markdown("""
<style>
.main {
    padding-top: 1rem;
}

.hero {
    background: linear-gradient(135deg, #4F46E5, #7C3AED);
    padding: 2rem;
    border-radius: 15px;
    color: white;
    text-align: center;
    margin-bottom: 2rem;
}

.feature-card {
    background: #f8fafc;
    padding: 1rem;
    border-radius: 10px;
    border: 1px solid #e2e8f0;
    margin-bottom: 1rem;
}

.metric-box {
    background: white;
    padding: 1rem;
    border-radius: 10px;
    border: 1px solid #e5e7eb;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# SESSION STATE
# -----------------------------
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if "user" not in st.session_state:
    st.session_state.user = None

# -----------------------------
# SIDEBAR
# -----------------------------
with st.sidebar:
    st.title("🎓 ExamPrep AI")

    st.markdown("---")

    if st.session_state.authenticated:
        st.success("Logged In ✅")

        st.info("""
        📚 Features

        • Dashboard
        • AI Quiz
        • Analytics
        • Study Plan
        • Videos
        • AI Mentor
        • Profile
        """)

    else:
        st.warning("Please Login")

    st.markdown("---")
    st.caption("Powered by Groq + OpenRouter + Supabase")

# -----------------------------
# HOME PAGE
# -----------------------------
st.markdown("""
<div class="hero">
    <h1>🎓 ExamPrep AI</h1>
    <h3>Your Personal AI Study Companion</h3>
    <p>Prepare smarter for JEE, NEET, UPSC, CAT, GATE and more.</p>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# FEATURES
# -----------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
        <h4>📝 AI Quiz Generator</h4>
        <p>Generate practice quizzes instantly by subject and topic.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <h4>📊 Performance Analytics</h4>
        <p>Track scores, strengths, weaknesses and progress.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <h4>🤖 AI Mentor</h4>
        <p>Ask doubts and receive personalized study guidance.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# -----------------------------
# SUPPORTED EXAMS
# -----------------------------
st.subheader("🎯 Supported Exams")

exam_col1, exam_col2, exam_col3, exam_col4 = st.columns(4)

with exam_col1:
    st.success("JEE")

with exam_col2:
    st.success("NEET")

with exam_col3:
    st.success("UPSC")

with exam_col4:
    st.success("CAT")

exam_col5, exam_col6, exam_col7, exam_col8 = st.columns(4)

with exam_col5:
    st.success("GATE")

with exam_col6:
    st.success("SSC")

with exam_col7:
    st.success("Banking")

with exam_col8:
    st.success("General")

st.markdown("---")

# -----------------------------
# QUICK STATS
# -----------------------------
st.subheader("📈 What You Can Do")

m1, m2, m3, m4 = st.columns(4)

with m1:
    st.metric(
        label="AI Quiz",
        value="Unlimited"
    )

with m2:
    st.metric(
        label="Study Plans",
        value="Personalized"
    )

with m3:
    st.metric(
        label="Video Recommendations",
        value="Smart"
    )

with m4:
    st.metric(
        label="AI Doubt Support",
        value="24/7"
    )

st.markdown("---")

# -----------------------------
# LOGIN REMINDER
# -----------------------------
if not st.session_state.authenticated:
    st.info(
        "👈 Please open the Login page from the Pages menu and sign in to continue."
    )

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("""
<hr>
<center>
<p>
🎓 ExamPrep AI <br>
Personalized Study Intelligence Platform
</p>
</center>
""", unsafe_allow_html=True)

from utils.supabase_client import supabase

try:
    result = supabase.table("profiles").select("*").execute()

    st.success("Supabase Connected Successfully ✅")
    st.write(result.data)

except Exception as e:
    st.error(f"Supabase Error: {e}")