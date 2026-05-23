# AI-Powered FAQ Chatbot

This repository contains **Task 2** for the VedGrow Generative AI Internship.

## Task Title

**AI-Powered FAQ Chatbot**

## Objective

Build a chatbot using the OpenAI API that answers questions about a chosen topic.

## Chosen Topic

**AI Internship FAQ Assistant**

The chatbot answers beginner-friendly questions about:

- Internship tasks
- GitHub repository setup
- Task submission
- LinkedIn posting
- Streamlit deployment
- Beginner AI/ML learning guidance
- Prompt engineering and chatbot project guidance

## Features

This project satisfies all task requirements:

| Requirement | Status |
|---|---|
| System prompt defining bot persona and knowledge domain | Completed |
| Multi-turn conversation memory using last 5 messages | Completed |
| Web UI with chat interface | Completed using Streamlit |
| Fallback for out-of-scope questions | Completed |
| API key secured in environment variables | Completed |
| GitHub repo + live Streamlit/Hugging Face URL | Ready for deployment |

## Project Structure

```text
VedGrow_GAI_02/
│
├── app.py
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
└── sample_questions.md
```

## How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/your-username/VedGrow_GAI_02.git
cd VedGrow_GAI_02
```

### 2. Install requirements

```bash
pip install -r requirements.txt
```

### 3. Create a `.env` file

Create a `.env` file in the project folder and add your OpenAI API key:

```env
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL=gpt-5.5
```

Do not upload your `.env` file to GitHub.

### 4. Run the Streamlit app

```bash
streamlit run app.py
```

## Deployment on Streamlit Community Cloud

1. Upload this project to a public GitHub repository.
2. Go to Streamlit Community Cloud.
3. Create a new app.
4. Select your GitHub repository.
5. Set the main file path as:

```text
app.py
```

6. Add your API key in Streamlit secrets:

```toml
OPENAI_API_KEY = "your_openai_api_key_here"
OPENAI_MODEL = "gpt-5.5"
```

7. Deploy the app.
8. Copy the live Streamlit URL and submit it with your GitHub repository link.

## Example Questions

You can ask:

- How do I create a GitHub repository for my internship task?
- What should I include in my README file?
- How do I post my completed task on LinkedIn?
- How do I deploy a Streamlit app?
- What is prompt engineering?
- What is the difference between AI and ML?

## Out-of-Scope Fallback

If the user asks something unrelated, the bot responds with a fallback message explaining that it only answers questions about the AI internship, GitHub submission, LinkedIn posting, Streamlit deployment, and beginner AI/ML learning topics.

## Tools Used

- Python
- OpenAI API
- Streamlit
- python-dotenv

## Author

Rajesh A
