# utils/supabase_client.py

import os
from dotenv import load_dotenv
from supabase import create_client, Client

# --------------------------------------------------
# LOAD ENVIRONMENT VARIABLES
# --------------------------------------------------

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL:
    raise Exception("SUPABASE_URL not found in .env")

if not SUPABASE_KEY:
    raise Exception("SUPABASE_KEY not found in .env")

supabase: Client = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)

# ==================================================
# AUTH FUNCTIONS
# ==================================================

def sign_up(email: str, password: str):
    return supabase.auth.sign_up(
        {
            "email": email,
            "password": password
        }
    )


def sign_in(email: str, password: str):
    return supabase.auth.sign_in_with_password(
        {
            "email": email,
            "password": password
        }
    )


def sign_out():
    return supabase.auth.sign_out()


def get_current_user():
    try:
        return supabase.auth.get_user()
    except Exception as e:
        print("GET USER ERROR:", e)
        return None

# ==================================================
# PROFILE FUNCTIONS
# ==================================================

def create_profile(
    user_id,
    name,
    email,
    exam_type="General",
    daily_hours=4
):

    data = {
        "id": user_id,
        "name": name,
        "email": email,
        "exam_type": exam_type,
        "daily_hours": daily_hours
    }

    result = (
        supabase
        .table("profiles")
        .insert(data)
        .execute()
    )

    print("PROFILE CREATED:", result)

    return result


def get_profile(user_id):

    result = (
        supabase
        .table("profiles")
        .select("*")
        .eq("id", user_id)
        .execute()
    )

    if result.data:
        return result.data[0]

    return None


def update_profile(user_id, updates):

    result = (
        supabase
        .table("profiles")
        .update(updates)
        .eq("id", user_id)
        .execute()
    )

    return result

# ==================================================
# QUIZ RESULTS
# ==================================================

def save_quiz_result(
    user_id,
    subject,
    topic,
    score,
    total,
    time_taken=0
):

    data = {
        "user_id": user_id,
        "subject": subject,
        "topic": topic,
        "score": score,
        "total": total,
        "time_taken": time_taken
    }

    result = (
        supabase
        .table("quiz_results")
        .insert(data)
        .execute()
    )

    print("QUIZ SAVED:", result)

    return result


def get_quiz_results(user_id):

    result = (
        supabase
        .table("quiz_results")
        .select("*")
        .eq("user_id", user_id)
        .order("created_at", desc=True)
        .execute()
    )

    return result.data

# ==================================================
# STUDY PLANS
# ==================================================

def save_study_plan(user_id, plan):

    data = {
        "user_id": user_id,
        "plan": plan
    }

    result = (
        supabase
        .table("study_plans")
        .insert(data)
        .execute()
    )

    print("PLAN SAVED:", result)

    return result


def get_study_plans(user_id):

    result = (
        supabase
        .table("study_plans")
        .select("*")
        .eq("user_id", user_id)
        .order("created_at", desc=True)
        .execute()
    )

    return result.data

# ==================================================
# BOOKMARKS
# ==================================================

def add_bookmark(
    user_id,
    video_id,
    title,
    channel,
    topic="",
    thumbnail=""
):

    data = {
        "user_id": user_id,
        "video_id": video_id,
        "title": title,
        "channel": channel,
        "topic": topic,
        "thumbnail": thumbnail
    }

    result = (
        supabase
        .table("bookmarks")
        .insert(data)
        .execute()
    )

    print("BOOKMARK SAVED:", result)

    return result


def get_bookmarks(user_id):

    result = (
        supabase
        .table("bookmarks")
        .select("*")
        .eq("user_id", user_id)
        .execute()
    )

    return result.data

# ==================================================
# CHAT HISTORY
# ==================================================

def save_chat_message(
    user_id,
    role,
    content
):

    data = {
        "user_id": user_id,
        "role": role,
        "content": content
    }

    result = (
        supabase
        .table("chat_history")
        .insert(data)
        .execute()
    )

    print("CHAT SAVED:", result)

    return result


def get_chat_history(user_id):

    result = (
        supabase
        .table("chat_history")
        .select("*")
        .eq("user_id", user_id)
        .order("created_at")
        .execute()
    )

    return result.data