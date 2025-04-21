
import streamlit as st
import openai
import os

# Set your OpenAI API key here or in Streamlit Secrets
openai.api_key = st.secrets.get("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY")

# Load syllabus content (normally you'd store it externally or in a file)
syllabus_text = """
FINA 300 – Financial Management
Section 12: 9:05am – 10:00am
Spring 2025
Instructor: Dr. Marko Svetina
Office Hours: Monday & Friday 10:00am-11:30am or by Zoom appt
Email: msvetina@sandiego.edu
Classroom: KCBE 320
Final Exam: Wednesday, May 21, 2025 – 8am-10am
Grading: HW 15%, Midterms 40%, Participation 10%, Final 35%
Textbook: 'Fundamentals of Corporate Finance', 13th Ed.
No AI use allowed for homework or exams.
Class meets MWF, 9:05am–10:00am. Course content includes valuation, budgeting, CAPM, etc.
"""

# Streamlit App UI
st.title("🤖 FINA 300 SyllabusBot")
st.markdown("Ask me anything about your course syllabus!")

question = st.text_input("Your question:", placeholder="e.g., When is the final exam?")

if question:
    with st.spinner("Thinking..."):
        prompt = f"""
You are a helpful assistant for a college course. A student asks a question about their syllabus. Answer based on the text below:

Syllabus:
{syllabus_text}

Question: {question}
Answer:
"""
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
            max_tokens=500
        )
        
        answer = response.choices[0].message.content.strip()
        st.success(answer)
