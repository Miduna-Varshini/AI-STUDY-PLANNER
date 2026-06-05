# utils/ai_client.py

import os
from dotenv import load_dotenv
from groq import Groq
import requests

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# --------------------------------------------------
# GROQ CLIENT
# --------------------------------------------------

groq_client = None

if GROQ_API_KEY:
    groq_client = Groq(api_key=GROQ_API_KEY)


# --------------------------------------------------
# GENERIC GROQ CHAT
# --------------------------------------------------

def groq_chat(prompt, model="llama-3.3-70b-versatile"):
    """
    General chat function
    """

    try:

        completion = groq_client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.7,
            max_tokens=2048
        )

        return completion.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}"


# --------------------------------------------------
# OPENROUTER FALLBACK
# --------------------------------------------------

def openrouter_chat(
    prompt,
    model="deepseek/deepseek-chat-v3"
):

    try:

        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": model,
                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            },
            timeout=60
        )

        data = response.json()

        return data["choices"][0]["message"]["content"]

    except Exception as e:
        return f"Error: {str(e)}"


# --------------------------------------------------
# SMART AI CALL
# --------------------------------------------------

def ask_ai(prompt):

    if GROQ_API_KEY:
        return groq_chat(prompt)

    if OPENROUTER_API_KEY:
        return openrouter_chat(prompt)

    return "No AI API key configured."


# --------------------------------------------------
# QUIZ GENERATOR
# --------------------------------------------------

def generate_quiz(
    exam,
    subject,
    topic,
    num_questions=10
):

    prompt = f"""
You are an expert exam coach.

Generate {num_questions} multiple-choice questions.

Exam: {exam}
Subject: {subject}
Topic: {topic}

Format:

Q1.
Question

A)
B)
C)
D)

Answer: X

Only generate questions.
"""

    return ask_ai(prompt)


# --------------------------------------------------
# STUDY PLAN GENERATOR
# --------------------------------------------------

def generate_study_plan(
    exam,
    exam_date,
    daily_hours,
    weak_topics
):

    prompt = f"""
Create a personalized study plan.

Exam: {exam}
Exam Date: {exam_date}
Daily Study Hours: {daily_hours}

Weak Topics:
{weak_topics}

Requirements:

1. Daily schedule
2. Weekly targets
3. Revision strategy
4. Mock test strategy
5. Final preparation plan

Return a clean formatted plan.
"""

    return ask_ai(prompt)


# --------------------------------------------------
# AI MENTOR
# --------------------------------------------------

def mentor_chat(
    user_question,
    exam="General"
):

    prompt = f"""
You are ExamPrep AI Mentor.

Student Exam:
{exam}

Student Question:
{user_question}

Provide:

1. Simple explanation
2. Exam-focused answer
3. Tips
4. Motivation

Keep response structured.
"""

    return ask_ai(prompt)


# --------------------------------------------------
# PERFORMANCE ANALYSIS
# --------------------------------------------------

def analyze_performance(
    quiz_data
):

    prompt = f"""
Analyze the following student performance data.

{quiz_data}

Provide:

1. Strengths
2. Weaknesses
3. Topics needing improvement
4. Recommended study strategy
5. Expected performance trend

Keep it concise.
"""

    return ask_ai(prompt)


# --------------------------------------------------
# REVISION PLAN
# --------------------------------------------------

def generate_revision_plan(
    exam,
    weak_topics
):

    prompt = f"""
Create a revision plan.

Exam:
{exam}

Weak Topics:
{weak_topics}

Provide:

- 7 Day Revision Plan
- Daily Tasks
- Practice Questions Recommendation
- Mock Test Schedule
"""

    return ask_ai(prompt)


# --------------------------------------------------
# DAILY MOTIVATION
# --------------------------------------------------

def get_motivation(exam):

    prompt = f"""
Give one powerful motivational message for a student preparing for {exam}.

Maximum 100 words.
"""

    return ask_ai(prompt)
