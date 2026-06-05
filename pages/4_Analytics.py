# pages/4_Analytics.py

import streamlit as st
import pandas as pd
import plotly.express as px

from utils.supabase_client import get_quiz_results
from utils.ai_client import analyze_performance

from components.styles import (
    load_css,
    hero_section,
    footer
)

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Analytics | ExamPrep AI",
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

user = st.session_state.get("user")

if not user:
    st.error("User session not found.")
    st.stop()

# --------------------------------------------------
# HEADER
# --------------------------------------------------

hero_section(
    "📊 Performance Analytics",
    "Track progress and identify improvement areas."
)

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

quiz_results = get_quiz_results(user.id)

if not quiz_results:
    st.info("No quiz data available yet.")
    footer()
    st.stop()

df = pd.DataFrame(quiz_results)

# --------------------------------------------------
# CLEAN DATA
# --------------------------------------------------

if "percentage" in df.columns:
    df["percentage"] = pd.to_numeric(
        df["percentage"],
        errors="coerce"
    )

# --------------------------------------------------
# METRICS
# --------------------------------------------------

st.subheader("📈 Overall Statistics")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Quizzes",
        len(df)
    )

with col2:
    st.metric(
        "Average Score",
        f"{round(df['percentage'].mean(),2)}%"
    )

with col3:
    st.metric(
        "Best Score",
        f"{round(df['percentage'].max(),2)}%"
    )

# --------------------------------------------------
# SCORE TREND
# --------------------------------------------------

st.subheader("📉 Score Trend")

if "created_at" in df.columns:

    df["created_at"] = pd.to_datetime(
        df["created_at"]
    )

    df = df.sort_values(
        "created_at"
    )

    fig = px.line(
        df,
        x="created_at",
        y="percentage",
        markers=True,
        title="Quiz Performance Over Time"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# --------------------------------------------------
# SUBJECT ANALYSIS
# --------------------------------------------------

if "subject" in df.columns:

    st.subheader("📚 Subject-wise Performance")

    subject_avg = (
        df.groupby("subject")["percentage"]
        .mean()
        .reset_index()
    )

    fig = px.bar(
        subject_avg,
        x="subject",
        y="percentage",
        title="Average Score by Subject"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# --------------------------------------------------
# TOPICS ANALYSIS
# --------------------------------------------------

if "topic" in df.columns:

    st.subheader("🎯 Topic-wise Performance")

    topic_avg = (
        df.groupby("topic")["percentage"]
        .mean()
        .reset_index()
        .sort_values(
            "percentage",
            ascending=False
        )
    )

    fig = px.bar(
        topic_avg,
        x="topic",
        y="percentage",
        title="Topic Performance"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# --------------------------------------------------
# WEAK TOPICS
# --------------------------------------------------

st.subheader("⚠️ Weak Topics")

weak_topics = []

if "topic" in df.columns:

    topic_avg = (
        df.groupby("topic")["percentage"]
        .mean()
        .reset_index()
    )

    weak_topics_df = topic_avg[
        topic_avg["percentage"] < 60
    ]

    if not weak_topics_df.empty:

        weak_topics = (
            weak_topics_df["topic"]
            .tolist()
        )

        for topic in weak_topics:
            st.warning(topic)

    else:
        st.success(
            "No major weak topics detected."
        )

# --------------------------------------------------
# RECENT RESULTS TABLE
# --------------------------------------------------

st.subheader("📝 Quiz History")

display_cols = [
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
    df[display_cols],
    use_container_width=True
)

# --------------------------------------------------
# AI ANALYSIS
# --------------------------------------------------

st.subheader("🤖 AI Performance Report")

try:

    sample_data = df.tail(15).to_dict(
        orient="records"
    )

    ai_report = analyze_performance(
        str(sample_data)
    )

    st.markdown(ai_report)

except Exception as e:

    st.error(
        f"AI analysis failed: {e}"
    )

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

footer()