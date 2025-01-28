import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as gen_ai # not working

# Load environment variables
load_dotenv()

# Configure Streamlit page
st.set_page_config(
    page_title="Study Destination Assistant",
    page_icon="🎓",
    layout="centered"
)

# Google Gemini Pro API Key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure Google Gemini Pro
gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel('gemini-pro')

# Initialize the chat session
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

# Display title and description
st.title("🎓 Study Destination Assistant")
st.markdown("Welcome! I'm here to assist you in finding the perfect study destination based on your preferences. Ask me questions or fill out the form below to get personalized recommendations!")

# Utility functions
def get_study_recommendations(country, subject, intake):
    """
    Mock function to fetch study recommendations.
    Replace this with actual database queries or API calls.
    """
    recommendations = {
        "UK": ["University of Oxford", "University of Cambridge", "Imperial College London"],
        "USA": ["Harvard University", "Stanford University", "MIT"],
        "Canada": ["University of Toronto", "University of British Columbia", "McGill University"]
    }
    return recommendations.get(country, ["No recommendations available."])

def handle_study_query(prompt):
    """
    Handles specific queries about study destinations.
    """
    if "study destination" in prompt.lower():
        return "I can help you find a study destination! Please provide your preferred country, subject, and intake."
    elif "country" in prompt.lower() or "subject" in prompt.lower():
        return "Thanks for the details! Let me check for recommendations."
    return None

# Chat interface
st.subheader("💬 Chat with Gemini-Pro")
for message in st.session_state.chat_session.history:
    with st.chat_message("assistant" if message.role == "model" else "user"):
        st.markdown(message.parts[0].text)

user_prompt = st.chat_input("Ask about study destinations...")
if user_prompt:
    # Add user input to chat history
    st.chat_message("user").markdown(user_prompt)

    # Handle specific queries about study destinations
    custom_response = handle_study_query(user_prompt)
    if custom_response:
        with st.chat_message("assistant"):
            st.markdown(custom_response)
    else:
        # Send input to Gemini-Pro for a response
        gemini_response = st.session_state.chat_session.send_message(user_prompt)
        with st.chat_message("assistant"):
            st.markdown(gemini_response.text)

# Preference form
st.subheader("📋 Fill Out Your Preferences")
with st.form("preferences_form"):
    country = st.selectbox("Preferred country:", ["UK", "USA", "Canada"])
    subject = st.text_input("Preferred subject (e.g., Computer Science, Medicine):")
    intake = st.text_input("Preferred intake (e.g., Fall 2025):")
    submit_button = st.form_submit_button("Get Recommendations")

if submit_button:
    # Get recommendations based on preferences
    recommendations = get_study_recommendations(country, subject, intake)
    st.subheader("🎓 Top Recommendations")
    if recommendations:
        st.markdown(f"Here are the top universities for **{subject}** in **{country}** (Intake: {intake}):")
        for uni in recommendations:
            st.markdown(f"- {uni}")
    else:
        st.markdown("Sorry, no recommendations found for your preferences.")

# Conclusion
st.divider()
st.markdown("Feel free to ask more questions or adjust your preferences to explore other study destinations!")
