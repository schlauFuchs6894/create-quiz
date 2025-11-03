import streamlit as st
import json
import uuid

st.title("🧠 Freundschaftsquiz erstellen")

quiz_data = []

for i in range(1, 11):
    st.subheader(f"Frage {i}")
    question = st.text_input(f"Frage {i} eingeben", key=f"q{i}")
    options = [st.text_input(f"Antwort {j+1}", key=f"q{i}_opt{j}") for j in range(4)]
    correct = st.radio("Richtige Antwort auswählen", options, key=f"q{i}_correct")
    
    quiz_data.append({
        "question": question,
        "options": options,
        "correct": correct
    })

if st.button("Quiz speichern"):
    quiz_id = str(uuid.uuid4())[:6]
    with open(f"quiz_{quiz_id}.json", "w", encoding="utf-8") as f:
        json.dump(quiz_data, f, ensure_ascii=False, indent=2)
    st.success(f"Quiz gespeichert! Teile diesen Link mit deinen Freunden:")
    st.code(f"https://deine-app-url.com/play_quiz?code={quiz_id}")
