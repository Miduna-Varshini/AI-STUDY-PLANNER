# utils/youtube_client.py

import os
from dotenv import load_dotenv
from googleapiclient.discovery import build

load_dotenv()

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

youtube = None

if YOUTUBE_API_KEY:
    youtube = build(
        "youtube",
        "v3",
        developerKey=YOUTUBE_API_KEY
    )


# =====================================================
# SEARCH VIDEOS
# =====================================================

def search_videos(
    query,
    max_results=10
):
    """
    Search educational videos
    """

    try:

        request = youtube.search().list(
            q=query,
            part="snippet",
            type="video",
            maxResults=max_results
        )

        response = request.execute()

        videos = []

        for item in response.get("items", []):

            snippet = item["snippet"]

            videos.append({
                "video_id": item["id"]["videoId"],
                "title": snippet["title"],
                "channel": snippet["channelTitle"],
                "description": snippet["description"],
                "thumbnail": snippet["thumbnails"]["high"]["url"],
                "published_at": snippet["publishedAt"],
                "url": f"https://www.youtube.com/watch?v={item['id']['videoId']}"
            })

        return videos

    except Exception as e:
        print("YouTube Search Error:", e)
        return []


# =====================================================
# TOPIC VIDEO SEARCH
# =====================================================

def search_topic_videos(
    exam,
    subject,
    topic,
    max_results=10
):
    """
    Search based on exam + subject + topic
    """

    query = f"{exam} {subject} {topic}"

    return search_videos(
        query=query,
        max_results=max_results
    )


# =====================================================
# WEAK TOPIC VIDEOS
# =====================================================

def get_weak_topic_videos(
    weak_topic,
    max_results=10
):
    """
    Search videos for weak areas
    """

    query = f"{weak_topic} full explanation"

    return search_videos(
        query=query,
        max_results=max_results
    )


# =====================================================
# REVISION VIDEOS
# =====================================================

def get_revision_videos(
    exam,
    subject,
    max_results=10
):

    query = f"{exam} {subject} revision"

    return search_videos(
        query=query,
        max_results=max_results
    )


# =====================================================
# MOCK TEST VIDEOS
# =====================================================

def get_mock_test_videos(
    exam,
    max_results=10
):

    query = f"{exam} mock test strategy"

    return search_videos(
        query=query,
        max_results=max_results
    )


# =====================================================
# STUDY MOTIVATION VIDEOS
# =====================================================

def get_motivation_videos(
    exam,
    max_results=10
):

    query = f"{exam} motivation for students"

    return search_videos(
        query=query,
        max_results=max_results
    )


# =====================================================
# VIDEO DETAILS
# =====================================================

def get_video_details(video_id):

    try:

        request = youtube.videos().list(
            part="snippet,statistics",
            id=video_id
        )

        response = request.execute()

        if not response["items"]:
            return None

        item = response["items"][0]

        return {
            "title": item["snippet"]["title"],
            "channel": item["snippet"]["channelTitle"],
            "views": item["statistics"].get("viewCount", 0),
            "likes": item["statistics"].get("likeCount", 0),
            "thumbnail": item["snippet"]["thumbnails"]["high"]["url"]
        }

    except Exception as e:
        print("Video Detail Error:", e)
        return None


# =====================================================
# TRENDING EDUCATION VIDEOS
# =====================================================

def get_trending_education_videos(
    max_results=10
):

    try:

        request = youtube.search().list(
            q="education learning",
            part="snippet",
            type="video",
            maxResults=max_results,
            order="viewCount"
        )

        response = request.execute()

        videos = []

        for item in response["items"]:

            snippet = item["snippet"]

            videos.append({
                "video_id": item["id"]["videoId"],
                "title": snippet["title"],
                "channel": snippet["channelTitle"],
                "thumbnail": snippet["thumbnails"]["high"]["url"],
                "url": f"https://www.youtube.com/watch?v={item['id']['videoId']}"
            })

        return videos

    except Exception:
        return []