from app.voice_io import speak, listen
from app.groq_api import ask_llm

class VoiceInterview:
    def __init__(self):
        self.topics = [
            "LLM", "NLP", "Deep Learning", "Machine Learning",
            "Agentic AI", "PyTorch", "Python", "Data Science"
        ]
        self.history = []

    def generate_question(self):
        topic_str = ", ".join(self.topics)
        q_prompt = f"""
You are an AI interviewer. Topics allowed: {topic_str}.
Conversation history: {self.history}

Ask ONE clear question to the user about these topics.
Question must be maximum 15 words.
Do not exceed 15 words.
"""
        question = ask_llm(q_prompt)

        # Safety truncation
        question_words = question.split()
        if len(question_words) > 15:
            question = " ".join(question_words[:15])
        return question

    def evaluate_answer(self, answer):
        eval_prompt = f"""
User answer: {answer}
Topics: {', '.join(self.topics)}

Provide feedback in maximum 40 words:
1. Correct points
2. Missing/wrong points
3. Suggestions for improvement
Do not exceed 40 words.
"""
        feedback = ask_llm(eval_prompt)

        # Safety truncation
        feedback_words = feedback.split()
        if len(feedback_words) > 40:
            feedback = " ".join(feedback_words[:40])
        return feedback

    def start_conversation(self, stop_callback):
        speak(f"Hello! Welcome to your AI interview. Let's start.")
        while True:
            if stop_callback():
                speak("Ending interview. Goodbye!")
                break

            question = self.generate_question()
            speak(question)
            print(f"AI: {question}")

            answer = listen()
            if not answer.strip():
                continue

            feedback = self.evaluate_answer(answer)
            self.history.append({"question": question, "answer": answer, "feedback": feedback})
            speak(feedback)
            print(f"Feedback: {feedback}")
