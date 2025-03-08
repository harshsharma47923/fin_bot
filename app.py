import streamlit as st
import google.generativeai as genai  # Import Gemini API
from time import sleep

# Set Gemini API Key (Replace 'your-api-key' with a valid one)
API_KEY = "AIzaSyAFh7vzUDL5V9KZhcSJq4uxxhmCX2JQnnU"  # Replace with your actual API key

genai.configure(api_key=API_KEY)

def get_available_models():
    """Fetch available Gemini models"""
    try:
        models = genai.list_models()
        return [model.name for model in models if "generateContent" in model.supported_generation_methods and "vision" not in model.name.lower()]
    except Exception as e:
        st.error(f"Error fetching models: {e}")
        return ["gemini-pro"]

AVAILABLE_MODELS = get_available_models()

def chatbot_response(prompt, model_name):
    """Get response from Gemini API"""
    try:
        model = genai.GenerativeModel(model_name)
        with st.spinner("💵 Fin Bot is analyzing the market..."):
            sleep(1)  # Simulate a delay for better UX
            response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        st.error(f"Error generating response: {e}")
        return "❌ Error: Please check API quota and billing details."

# Streamlit UI
st.set_page_config(page_title="Fin Bot", layout="wide")

st.markdown(
    """
    <div style='text-align: center;'>
        <img src='https://cdn-icons-png.flaticon.com/512/2906/2906277.png' width='150'>
        <h1 style='color: #6A0572;'>📈 Fin Bot 💹</h1>
        <p style='font-size:20px; font-weight: bold; color: #333;'>Your AI Assistant for Finance, Stocks & Investments</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Sidebar
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/2332/2332591.png", width=120)
st.sidebar.header("💼 Settings")
model_choice = st.sidebar.selectbox("🏦 Select Model", AVAILABLE_MODELS)

if st.sidebar.button("🗑️ Clear Chat"):
    st.session_state.chat_history = []

st.sidebar.markdown("---")
st.sidebar.markdown(
    """
    <div style='text-align: center;'>
        <p style='font-size:16px;'><b>Developed by Harsh Sharma</b></p>
        <p style='font-size:14px;'>Pursuing MBA in Fintech</p>
        <img src='https://cdn-icons-png.flaticon.com/512/3312/3312351.png' width='80'>
    </div>
    """,
    unsafe_allow_html=True,
)

# Chat Interface
chat_history = st.session_state.get("chat_history", [])
user_input = st.text_input("💰 Type your financial query:")

if st.button("📊 Analyze") and user_input:
    chat_history.append(("You", user_input))
    response = chatbot_response(user_input, model_choice)
    chat_history.append(("Fin Bot", response))
    st.session_state.chat_history = chat_history

# Display Chat History
st.markdown("### 💬 Chat History")
for sender, message in chat_history:
    role = "🟢 **Fin Bot:**" if sender == "Fin Bot" else "🔵 **You:**"
    st.markdown(f"{role} {message}")
