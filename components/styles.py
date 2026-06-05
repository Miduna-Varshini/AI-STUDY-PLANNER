# components/styles.py

import streamlit as st


def load_css():
    st.markdown(
        """
        <style>

        /* =========================
           GLOBAL
        ========================= */

        .main {
            padding-top: 1rem;
        }

        .block-container {
            padding-top: 1rem;
            padding-bottom: 2rem;
        }

        h1, h2, h3, h4 {
            font-weight: 700;
        }

        /* =========================
           HERO SECTION
        ========================= */

        .hero {
            background: linear-gradient(
                135deg,
                #4f46e5,
                #7c3aed
            );
            color: white;
            padding: 2rem;
            border-radius: 20px;
            text-align: center;
            margin-bottom: 20px;
        }

        .hero h1 {
            color: white;
        }

        .hero p {
            font-size: 18px;
        }

        /* =========================
           CARDS
        ========================= */

        .card {
            background: white;
            padding: 20px;
            border-radius: 15px;
            border: 1px solid #e5e7eb;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
            margin-bottom: 15px;
        }

        /* =========================
           METRICS
        ========================= */

        .metric-card {
            background: #f8fafc;
            border: 1px solid #e5e7eb;
            border-radius: 15px;
            padding: 15px;
            text-align: center;
        }

        .metric-value {
            font-size: 28px;
            font-weight: bold;
            color: #4f46e5;
        }

        .metric-label {
            color: #64748b;
            font-size: 14px;
        }

        /* =========================
           QUIZ
        ========================= */

        .quiz-box {
            background: #f8fafc;
            border-left: 5px solid #4f46e5;
            padding: 15px;
            border-radius: 10px;
            margin-bottom: 10px;
        }

        /* =========================
           SUCCESS
        ========================= */

        .success-box {
            background: #ecfdf5;
            border: 1px solid #10b981;
            color: #065f46;
            padding: 15px;
            border-radius: 12px;
            margin-bottom: 15px;
        }

        /* =========================
           WARNING
        ========================= */

        .warning-box {
            background: #fffbeb;
            border: 1px solid #f59e0b;
            color: #92400e;
            padding: 15px;
            border-radius: 12px;
            margin-bottom: 15px;
        }

        /* =========================
           DANGER
        ========================= */

        .danger-box {
            background: #fef2f2;
            border: 1px solid #ef4444;
            color: #991b1b;
            padding: 15px;
            border-radius: 12px;
            margin-bottom: 15px;
        }

        /* =========================
           AI RESPONSE
        ========================= */

        .ai-box {
            background: #eef2ff;
            border-left: 5px solid #6366f1;
            padding: 20px;
            border-radius: 10px;
            margin-top: 10px;
            margin-bottom: 10px;
        }

        /* =========================
           VIDEO CARD
        ========================= */

        .video-card {
            border: 1px solid #e5e7eb;
            border-radius: 15px;
            padding: 15px;
            margin-bottom: 15px;
        }

        .video-title {
            font-weight: bold;
            font-size: 16px;
        }

        .video-channel {
            color: #64748b;
            font-size: 13px;
        }

        /* =========================
           SIDEBAR
        ========================= */

        section[data-testid="stSidebar"] {
            border-right: 1px solid #e5e7eb;
        }

        /* =========================
           BUTTONS
        ========================= */

        .stButton > button {
            width: 100%;
            border-radius: 10px;
            font-weight: 600;
        }

        /* =========================
           FOOTER
        ========================= */

        .footer {
            text-align: center;
            color: gray;
            margin-top: 30px;
            font-size: 14px;
        }

        </style>
        """,
        unsafe_allow_html=True
    )


def hero_section(title, subtitle):
    st.markdown(
        f"""
        <div class="hero">
            <h1>{title}</h1>
            <p>{subtitle}</p>
        </div>
        """,
        unsafe_allow_html=True
    )


def card(content):
    st.markdown(
        f"""
        <div class="card">
            {content}
        </div>
        """,
        unsafe_allow_html=True
    )


def ai_response_box(content):
    st.markdown(
        f"""
        <div class="ai-box">
            {content}
        </div>
        """,
        unsafe_allow_html=True
    )


def success_box(content):
    st.markdown(
        f"""
        <div class="success-box">
            {content}
        </div>
        """,
        unsafe_allow_html=True
    )


def warning_box(content):
    st.markdown(
        f"""
        <div class="warning-box">
            {content}
        </div>
        """,
        unsafe_allow_html=True
    )


def danger_box(content):
    st.markdown(
        f"""
        <div class="danger-box">
            {content}
        </div>
        """,
        unsafe_allow_html=True
    )


def footer():
    st.markdown(
        """
        <div class="footer">
            🎓 ExamPrep AI • Personalized Study Intelligence
        </div>
        """,
        unsafe_allow_html=True
    )