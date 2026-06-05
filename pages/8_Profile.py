# pages/8_Profile.py

import streamlit as st
from datetime import date

from utils.supabase_client import (
    get_profile,
    update_profile,
    create_profile
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
    page_title="Profile | ExamPrep AI",
    page_icon="👤",
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

# If profile doesn't exist, create one
if not profile:

    try:

        create_profile(
            user_id=user.id,
            name=user.user_metadata.get("name", ""),
            email=user.email,
            exam_type="General",
            daily_hours=4
        )

        profile = get_profile(user.id)

    except Exception as e:

        st.error(f"Profile creation failed: {e}")
        st.stop()

# Still not found
if not profile:

    st.error("Unable to load profile.")
    st.stop()

# --------------------------------------------------
# HEADER
# --------------------------------------------------

hero_section(
    "👤 My Profile",
    "Manage your study preferences and exam settings."
)

# --------------------------------------------------
# PROFILE FORM
# --------------------------------------------------

name = st.text_input(
    "Full Name",
    value=profile.get("name", "")
)

email = st.text_input(
    "Email",
    value=profile.get("email", ""),
    disabled=True
)

exam_type = st.selectbox(
    "Exam Type",
    [
        "JEE",
        "NEET",
        "UPSC",
        "CAT",
        "GATE",
        "SSC",
        "Banking",
        "General"
    ],
)

exam_date = st.date_input(
    "Exam Date",
    value=date.today()
)

daily_hours = st.slider(
    "Daily Study Hours",
    1,
    12,
    int(profile.get("daily_hours", 4))
)

# --------------------------------------------------
# SAVE PROFILE
# --------------------------------------------------

if st.button("💾 Save Changes"):

    try:

        update_profile(
            user.id,
            {
                "name": name,
                "exam_type": exam_type,
                "exam_date": str(exam_date),
                "daily_hours": daily_hours
            }
        )

        st.success(
            "Profile updated successfully!"
        )

    except Exception as e:

        st.error(str(e))

# --------------------------------------------------
# SUMMARY
# --------------------------------------------------

st.markdown("---")

st.subheader("Profile Summary")

st.write("👤 Name:", name)
st.write("📧 Email:", email)
st.write("🎯 Exam:", exam_type)
st.write("📅 Exam Date:", exam_date)
st.write("⏰ Study Hours:", daily_hours)

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

footer()