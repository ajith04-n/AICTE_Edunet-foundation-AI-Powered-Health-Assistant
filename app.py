import streamlit as st
from transformers import pipeline
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

chatbot = pipeline("text-generation", model="gpt2")

def healthcare_chatbot(user_input):
    if "symptom" in user_input.lower():
        return "It seems like you're experiencing symptoms. Please consult a doctor for accurate advice."
    elif "appointment" in user_input.lower():
        return "Would you like me to schedule an appointment with a doctor?"
    elif "medication" in user_input.lower():
        return "It's important to take your prescribed medications regularly. If you have concerns, consult your doctor."
    elif "fever" in user_input.lower():
        return "If you have a fever, it's important to rest and stay hydrated. Over-the-counter medications like acetaminophen (Tylenol) or ibuprofen (Advil) can help reduce fever. If your fever persists or is very high, please consult a doctor."
    elif "back pain" in user_input.lower():
        return "For back pain, it's important to maintain good posture and avoid heavy lifting. Over-the-counter pain relievers like ibuprofen can help. If the pain persists, please consult a doctor."
    elif "headache" in user_input.lower():
        return "For headaches, staying hydrated and resting in a quiet, dark room can help. Over-the-counter pain relievers like acetaminophen or ibuprofen can also be effective. If headaches are frequent or severe, please consult a doctor."
    elif "cold" in user_input.lower():
        return "For a common cold, rest and stay hydrated. Over-the-counter medications can help relieve symptoms. If symptoms persist or worsen, please consult a doctor."
    else:
        response = chatbot(user_input, max_length=50, num_return_sequences=1)
        generated_text = response[0]['generated_text']
        if "fever" in generated_text.lower() or "symptom" in generated_text.lower():
            return generated_text
        else:
            return "I'm not sure how to respond to that. Can you please provide more details?"
def main():
    st.title("Healthcare Assistant Chatbot")
    user_input = st.text_input("How can I assist you today?", "")
    if st.button("Submit"):
        if user_input:
            st.write("User: ", user_input)
            with st.spinner("Processing your query, please wait..."):
                response = healthcare_chatbot(user_input)
            st.write("Healthcare Assistant: ", response)
        else:
            st.write("Please enter a query.")

if __name__ == "__main__":
    main()
