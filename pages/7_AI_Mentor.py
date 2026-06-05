# pages/7_AI_Mentor.py

import streamlit as st

from utils.ai_client import mentor_chat

from utils.supabase_client import (
    save_chat_message,
    get_chat_history,
    get_profile
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
    page_title="AI Mentor | ExamPrep AI",
    page_icon="🤖",
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
# PROFILE
# --------------------------------------------------

profile = get_profile(user.id)

exam_type = "General"

if profile:
    exam_type = profile.get(
        "exam_type",
        "General"
    )

# --------------------------------------------------
# HEADER
# --------------------------------------------------

hero_section(
    "🤖 AI Mentor",
    "Ask doubts, get guidance, and improve your preparation."
)

# --------------------------------------------------
# LOAD CHAT HISTORY
# --------------------------------------------------

chat_history = get_chat_history(user.id)

# --------------------------------------------------
# DISPLAY OLD CHATS
# --------------------------------------------------

st.subheader("💬 Conversation")

if chat_history:

    for msg in chat_history:

        role = msg.get("role", "")

        if role == "user":
            with st.chat_message("user"):
                st.markdown(
                    msg.get("content", "")
                )

        else:
            with st.chat_message("assistant"):
                st.markdown(
                    msg.get("content", "")
                )

# --------------------------------------------------
# NEW MESSAGE
# --------------------------------------------------

user_question = st.chat_input(
    "Ask your doubt..."
)

if user_question:

    # Show user message
    with st.chat_message("user"):
        st.markdown(user_question)

    # Save user message
    try:
        save_chat_message(
            user.id,
            "user",
            user_question
        )
    except Exception:
        pass

    # Generate AI response
    with st.spinner("Thinking..."):

        try:

            ai_response = mentor_chat(
                user_question=user_question,
                exam=exam_type
            )

        except Exception as e:

            ai_response = (
                f"Unable to generate response.\n\n{str(e)}"
            )

    # Show AI response
    with st.chat_message("assistant"):
        st.markdown(ai_response)

    # Save AI response
    try:

        save_chat_message(
            user.id,
            "assistant",
            ai_response
        )

    except Exception:
        pass

# --------------------------------------------------
# QUICK QUESTIONS
# --------------------------------------------------

st.markdown("---")

st.subheader("⚡ Quick Questions")

quick_questions = [
    "How should I prepare for my exam?",
    "Create a revision strategy.",
    "How can I improve weak topics?",
    "Give me motivation for studying.",
    "Suggest a daily study schedule."
]

for question in quick_questions:

    if st.button(question):

        with st.spinner("Generating answer..."):

            try:

                answer = mentor_chat(
                    user_question=question,
                    exam=exam_type
                )

                st.markdown("### Answer")
                st.markdown(answer)

            except Exception as e:

                st.error(str(e))

# --------------------------------------------------
# CLEAR CHAT INFO
# --------------------------------------------------

st.markdown("---")

st.info(
    "All conversations are automatically saved to your account."
)

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

footer()