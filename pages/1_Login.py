# pages/1_Login.py

import streamlit as st

from utils.supabase_client import (
    sign_up,
    sign_in,
    create_profile,
    get_profile,
    sign_out
)

from components.styles import (
    load_css,
    hero_section
)

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Login | ExamPrep AI",
    page_icon="🔐",
    layout="centered"
)

load_css()

hero_section(
    "🔐 Login / Register",
    "Access your personalized study dashboard"
)

# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if "user" not in st.session_state:
    st.session_state.user = None

# --------------------------------------------------
# ALREADY LOGGED IN
# --------------------------------------------------

if st.session_state.authenticated:

    st.success("You are already logged in.")

    if st.button("Logout"):

        sign_out()

        st.session_state.authenticated = False
        st.session_state.user = None

        st.rerun()

    st.stop()

# --------------------------------------------------
# TABS
# --------------------------------------------------

login_tab, signup_tab = st.tabs(
    ["Login", "Create Account"]
)

# ==================================================
# LOGIN
# ==================================================

with login_tab:

    st.subheader("Login")

    email = st.text_input(
        "Email",
        key="login_email"
    )

    password = st.text_input(
        "Password",
        type="password",
        key="login_password"
    )

    if st.button("Login"):

        if not email or not password:
            st.error("Please enter email and password.")
            st.stop()

        try:

            response = sign_in(
                email=email,
                password=password
            )

            user = response.user

            if user:

                st.session_state.authenticated = True
                st.session_state.user = user

                st.success("Login successful!")

                st.rerun()

            else:
                st.error("Invalid credentials.")

        except Exception as e:
            st.error(str(e))

# ==================================================
# SIGNUP
# ==================================================

with signup_tab:

    st.subheader("Create Account")

    name = st.text_input(
        "Full Name"
    )

    email = st.text_input(
        "Email Address"
    )

    password = st.text_input(
        "Password",
        type="password"
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
        ]
    )

    daily_hours = st.slider(
        "Daily Study Hours",
        min_value=1,
        max_value=12,
        value=4
    )

    if st.button("Create Account"):

        if not name:
            st.error("Name required.")
            st.stop()

        if not email:
            st.error("Email required.")
            st.stop()

        if not password:
            st.error("Password required.")
            st.stop()

        try:

            response = sign_up(
                email=email,
                password=password
            )

            user = response.user

            if user:

                create_profile(
                    user_id=user.id,
                    name=name,
                    email=email,
                    exam_type=exam_type,
                    daily_hours=daily_hours
                )

                st.success(
                    "Account created successfully."
                )

                st.info(
                    "Please verify your email if required, then login."
                )

            else:
                st.error(
                    "Unable to create account."
                )

        except Exception as e:
            st.error(str(e))

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown("---")

st.caption(
    "🎓 ExamPrep AI • Secure Authentication with Supabase"
)