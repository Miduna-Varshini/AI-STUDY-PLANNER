# pages/5_Study_Plan.py

import streamlit as st

from utils.supabase_client import (
    get_profile,
    save_study_plan,
    get_study_plans
)

from utils.ai_client import (
    generate_study_plan,
    generate_revision_plan
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
    page_title="Study Plan | ExamPrep AI",
    page_icon="📚",
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
# LOAD PROFILE
# --------------------------------------------------

profile = get_profile(user.id)

exam_type = "General"
daily_hours = 4

if profile:
    exam_type = profile.get(
        "exam_type",
        "General"
    )

    daily_hours = profile.get(
        "daily_hours",
        4
    )

# --------------------------------------------------
# HEADER
# --------------------------------------------------

hero_section(
    "📚 AI Study Planner",
    "Generate personalized study schedules and revision plans."
)

# --------------------------------------------------
# STUDY PLAN FORM
# --------------------------------------------------

st.subheader("Create New Study Plan")

col1, col2 = st.columns(2)

with col1:
    exam = st.text_input(
        "Exam",
        value=exam_type
    )

with col2:
    exam_date = st.date_input(
        "Exam Date"
    )

weak_topics = st.text_area(
    "Weak Topics (comma separated)",
    placeholder="Organic Chemistry, Thermodynamics, Probability"
)

daily_study_hours = st.slider(
    "Daily Study Hours",
    min_value=1,
    max_value=12,
    value=int(daily_hours)
)

# --------------------------------------------------
# GENERATE STUDY PLAN
# --------------------------------------------------

if st.button("Generate Study Plan"):

    with st.spinner(
        "Generating personalized plan..."
    ):

        try:

            plan = generate_study_plan(
                exam=exam,
                exam_date=str(exam_date),
                daily_hours=daily_study_hours,
                weak_topics=weak_topics
            )

            st.session_state.generated_plan = plan

            save_study_plan(
                user.id,
                plan
            )

            st.success(
                "Study plan generated successfully."
            )

        except Exception as e:

            st.error(str(e))

# --------------------------------------------------
# DISPLAY GENERATED PLAN
# --------------------------------------------------

if "generated_plan" in st.session_state:

    st.subheader(
        "🎯 Generated Study Plan"
    )

    st.markdown(
        st.session_state.generated_plan
    )

# --------------------------------------------------
# REVISION PLAN
# --------------------------------------------------

st.markdown("---")

st.subheader(
    "🔄 Generate Revision Plan"
)

revision_topics = st.text_area(
    "Revision Topics",
    placeholder="Calculus, Current Affairs, Biology"
)

if st.button(
    "Generate Revision Plan"
):

    with st.spinner(
        "Creating revision schedule..."
    ):

        try:

            revision_plan = (
                generate_revision_plan(
                    exam,
                    revision_topics
                )
            )

            st.markdown(
                revision_plan
            )

        except Exception as e:

            st.error(str(e))

# --------------------------------------------------
# PREVIOUS STUDY PLANS
# --------------------------------------------------

st.markdown("---")

st.subheader(
    "📂 Previous Study Plans"
)

plans = get_study_plans(
    user.id
)

if plans:

    for index, plan in enumerate(plans):

        title = (
            f"Plan {index + 1}"
        )

        if plan.get(
            "created_at"
        ):
            title = (
                f"Plan {index + 1} - "
                f"{plan['created_at'][:10]}"
            )

        with st.expander(title):

            st.markdown(
                plan.get(
                    "plan",
                    "No content"
                )
            )

else:

    st.info(
        "No study plans found."
    )

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

footer()