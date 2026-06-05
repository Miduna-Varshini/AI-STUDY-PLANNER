# pages/6_Videos.py

import streamlit as st

from utils.youtube_client import (
    search_topic_videos,
    get_revision_videos,
    get_motivation_videos
)

from utils.supabase_client import (
    add_bookmark,
    get_bookmarks,
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
    page_title="Videos | ExamPrep AI",
    page_icon="🎥",
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
    "🎥 Smart Video Learning",
    "Discover the best educational videos for your preparation."
)

# --------------------------------------------------
# SEARCH FORM
# --------------------------------------------------

st.subheader("🔍 Search Educational Videos")

col1, col2 = st.columns(2)

with col1:
    subject = st.text_input(
        "Subject",
        placeholder="Physics"
    )

with col2:
    topic = st.text_input(
        "Topic",
        placeholder="Newton Laws"
    )

if st.button("Search Videos"):

    if not subject or not topic:
        st.error(
            "Please enter subject and topic."
        )
        st.stop()

    with st.spinner(
        "Searching videos..."
    ):

        videos = search_topic_videos(
            exam_type,
            subject,
            topic,
            max_results=10
        )

        st.session_state.videos = videos

# --------------------------------------------------
# DISPLAY VIDEOS
# --------------------------------------------------

if "videos" in st.session_state:

    videos = st.session_state.videos

    if videos:

        st.subheader(
            "📺 Recommended Videos"
        )

        for video in videos:

            st.image(
                video["thumbnail"],
                width=300
            )

            st.markdown(
                f"### {video['title']}"
            )

            st.write(
                f"📺 Channel: {video['channel']}"
            )

            st.write(
                video["description"]
            )

            st.markdown(
                f"[▶ Watch Video]({video['url']})"
            )

            bookmark_key = (
                f"bookmark_"
                f"{video['video_id']}"
            )

            if st.button(
                "⭐ Save Bookmark",
                key=bookmark_key
            ):

                try:

                    add_bookmark(
                        user_id=user.id,
                        video_id=video["video_id"],
                        title=video["title"],
                        channel=video["channel"],
                        topic=topic,
                        thumbnail=video["thumbnail"]
                    )

                    st.success(
                        "Bookmark saved."
                    )

                except Exception as e:

                    st.error(str(e))

            st.markdown("---")

    else:

        st.info(
            "No videos found."
        )

# --------------------------------------------------
# REVISION VIDEOS
# --------------------------------------------------

st.subheader("📚 Revision Videos")

if st.button(
    "Show Revision Videos"
):

    revision_videos = (
        get_revision_videos(
            exam_type,
            subject if subject else "General"
        )
    )

    for video in revision_videos:

        st.markdown(
            f"**{video['title']}**"
        )

        st.write(
            video["channel"]
        )

        st.markdown(
            f"[Watch]({video['url']})"
        )

# --------------------------------------------------
# MOTIVATION VIDEOS
# --------------------------------------------------

st.subheader("🔥 Motivation Videos")

if st.button(
    "Show Motivation Videos"
):

    motivation_videos = (
        get_motivation_videos(
            exam_type
        )
    )

    for video in motivation_videos:

        st.markdown(
            f"**{video['title']}**"
        )

        st.write(
            video["channel"]
        )

        st.markdown(
            f"[Watch]({video['url']})"
        )

# --------------------------------------------------
# BOOKMARKS
# --------------------------------------------------

st.markdown("---")

st.subheader("⭐ My Bookmarks")

bookmarks = get_bookmarks(
    user.id
)

if bookmarks:

    for item in bookmarks:

        with st.expander(
            item.get(
                "title",
                "Video"
            )
        ):

            if item.get("thumbnail"):
                st.image(
                    item["thumbnail"],
                    width=250
                )

            st.write(
                f"📺 {item.get('channel', '')}"
            )

            st.write(
                f"📚 Topic: {item.get('topic', '')}"
            )

            video_url = (
                f"https://www.youtube.com/watch?v="
                f"{item['video_id']}"
            )

            st.markdown(
                f"[▶ Open Video]({video_url})"
            )

else:

    st.info(
        "No bookmarks available."
    )

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

footer()