import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

APP_TITLE = "AI-Powered FAQ Chatbot"
APP_SUBTITLE = "VedGrow GAI Task 2"

BOT_NAME = "AI Internship FAQ Assistant"
KNOWLEDGE_DOMAIN = """
You answer FAQs about an AI/Generative AI internship workflow.

Allowed topics:
- Internship task instructions
- GitHub repository setup and submissions
- LinkedIn task completion posts
- Project documentation
- Basic Python, AI, ML, prompt engineering, and chatbot learning guidance
- Streamlit deployment guidance
- Certificate and task completion guidance

Out-of-scope topics:
- Personal, legal, medical, financial, political, or unrelated questions
- Requests to reveal private API keys
- Questions unrelated to AI internship tasks or beginner AI learning
"""

SYSTEM_PROMPT = f"""
You are {BOT_NAME}, a friendly and beginner-focused FAQ chatbot.

Your knowledge domain:
{KNOWLEDGE_DOMAIN}

Behavior rules:
1. Answer only questions related to the allowed topics.
2. Give clear, short, practical answers for beginners.
3. If the question is out of scope, politely say:
   "I’m sorry, I can only answer questions about the AI internship, GitHub submission, LinkedIn posting, Streamlit deployment, and beginner AI/ML learning topics."
4. Never ask for or reveal API keys, passwords, private tokens, or sensitive personal information.
5. If the user asks about deadlines or official rules, remind them to verify with their internship email or official task document.
6. Use bullet points when helpful.
"""

FALLBACK_RESPONSE = (
    "I’m sorry, I can only answer questions about the AI internship, GitHub submission, "
    "LinkedIn posting, Streamlit deployment, and beginner AI/ML learning topics."
)


def get_api_key():
    """Get API key from Streamlit secrets or environment variables."""
    try:
        if "OPENAI_API_KEY" in st.secrets:
            return st.secrets["OPENAI_API_KEY"]
    except Exception:
        pass

    return os.getenv("OPENAI_API_KEY")


def get_model_name():
    """Get model from Streamlit secrets or environment variables."""
    try:
        if "OPENAI_MODEL" in st.secrets:
            return st.secrets["OPENAI_MODEL"]
    except Exception:
        pass

    return os.getenv("OPENAI_MODEL", "gpt-5.5")


def build_openai_messages(user_message):
    """
    Build the conversation sent to OpenAI.

    Requirement covered:
    - Multi-turn conversation memory using the last 5 messages.
    """
    recent_messages = st.session_state.messages[-5:]

    openai_messages = [
        {
            "role": "developer",
            "content": SYSTEM_PROMPT
        }
    ]

    for message in recent_messages:
        openai_messages.append(
            {
                "role": message["role"],
                "content": message["content"]
            }
        )

    openai_messages.append(
        {
            "role": "user",
            "content": user_message
        }
    )

    return openai_messages


def ask_chatbot(user_message):
    """Send user message and last 5 messages to OpenAI Responses API."""
    api_key = get_api_key()

    if not api_key:
        return (
            "API key is missing. Please add your OPENAI_API_KEY in a .env file locally "
            "or in Streamlit Cloud secrets before running this app."
        )

    try:
        client = OpenAI(api_key=api_key)
        model_name = get_model_name()

        response = client.responses.create(
            model=model_name,
            input=build_openai_messages(user_message),
            max_output_tokens=500
        )

        answer = response.output_text.strip()

        if not answer:
            return FALLBACK_RESPONSE

        return answer

    except Exception as error:
        return f"Sorry, something went wrong while generating the response: {error}"


# -----------------------
# Streamlit UI
# -----------------------

st.set_page_config(
    page_title=APP_TITLE,
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 AI-Powered FAQ Chatbot")
st.caption("Task 2 | Generative AI Internship | Built with Python, OpenAI API, and Streamlit")

with st.sidebar:
    st.header("About this chatbot")
    st.write(
        "This chatbot answers beginner-friendly FAQs about AI internship tasks, "
        "GitHub submission, LinkedIn posting, Streamlit deployment, and basic AI/ML learning."
    )

    st.subheader("Requirements Covered")
    st.markdown(
        """
        - System prompt with bot persona
        - Knowledge domain restriction
        - Last 5 messages memory
        - Streamlit web chat UI
        - Out-of-scope fallback
        - API key from environment variables
        """
    )

    if st.button("Clear chat"):
        st.session_state.messages = []
        st.rerun()

# Initialize message history.
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                "Hi! I’m your AI Internship FAQ Assistant. Ask me about internship tasks, "
                "GitHub submission, LinkedIn posts, Streamlit deployment, or beginner AI/ML topics."
            )
        }
    ]

# Display existing chat messages.
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input.
user_input = st.chat_input("Ask your FAQ question here...")

if user_input:
    # Show user message.
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # Generate and show assistant response.
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            assistant_response = ask_chatbot(user_input)
            st.write(assistant_response)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": assistant_response
        }
    )

    # Keep app memory small in browser session.
    # The OpenAI request itself uses only the last 5 messages.
    if len(st.session_state.messages) > 20:
        st.session_state.messages = st.session_state.messages[-20:]
