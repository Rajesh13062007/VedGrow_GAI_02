# Deployment Guide

## Deploying the AI-Powered FAQ Chatbot on Streamlit Community Cloud

### Step 1: Upload Files to GitHub

Create a public repository named:

```text
VedGrow_GAI_02
```

Upload these files:

```text
app.py
README.md
requirements.txt
.env.example
.gitignore
sample_questions.md
DEPLOYMENT.md
```

### Step 2: Create Streamlit App

1. Go to Streamlit Community Cloud.
2. Sign in using GitHub.
3. Click **New app**.
4. Select your repository.
5. Set the main file path:

```text
app.py
```

### Step 3: Add Secrets

In Streamlit app settings, open **Secrets** and add:

```toml
OPENAI_API_KEY = "your_openai_api_key_here"
OPENAI_MODEL = "gpt-5.5"
```

### Step 4: Deploy

Click **Deploy**.

After deployment, copy the live URL. Submit both:

1. GitHub repository URL
2. Live Streamlit app URL
