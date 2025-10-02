import streamlit as st
import speech_recognition as sr
from gtts import gTTS
import os
from app.groq_api import ask_llm

st.set_page_config(page_title="🤖 AI Interviewer", layout="centered")
st.title("🎤 AI Interviewer (Cloud Edition)")

st.markdown("This AI will ask you questions on **ML, DL, NLP, LLMs, Agentic AI, PyTorch, Python, Data Science**. "
            "Upload or record your answers, and the AI will evaluate them.")

# File uploader for audio input
uploaded_audio = st.file_uploader("🎙 Upload your answer (wav/mp3)", type=["wav", "mp3"])

if uploaded_audio is not None:
    recognizer = sr.Recognizer()
    with sr.AudioFile(uploaded_audio) as source:
        audio_data = recognizer.record(source)
        try:
            user_answer = recognizer.recognize_google(audio_data)
            st.success(f"🗣 You said: {user_answer}")

            # Ask Groq LLM for evaluation
            ai_response = ask_llm(
                f"You are an interviewer. Evaluate this answer on ML, DL, NLP, LLMs, "
                f"Agentic AI, PyTorch, Python, or Data Science. "
                f"Answer in max 40 words: {user_answer}"
            )

            st.info(f"🤖 AI: {ai_response}")

            # Convert AI answer to speech
            tts = gTTS(ai_response)
            tts.save("response.mp3")
            st.audio("response.mp3")

        except Exception as e:
            st.error(f"⚠️ Could not process audio: {e}")
