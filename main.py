import streamlit as st
from app.interview import VoiceInterview

st.set_page_config(page_title="Voice AI Interview", layout="centered")

st.title("🎙️ Voice AI Interviewer")
st.markdown("Your best Interview partner")

interview = VoiceInterview()

# Session state for stop
if 'stop' not in st.session_state:
    st.session_state.stop = False

def stop_callback():
    return st.session_state.stop

if st.button("Start Interview"):
    st.session_state.stop = False
    st.info("Interview started. Speak into your microphone.")
    interview.start_conversation(stop_callback)

if st.button("Stop Interview"):
    st.session_state.stop = True
    st.success("Interview stopped.")
