# AI-Mentalhealth-Chatbot
🌿 Mental Health Support Chatbot
A multi-turn AI companion powered by Gemini 2.5 Flash

💡 Overview

This project is an AI-driven mental health support chatbot that provides a safe space for users to express their thoughts and emotions.
It enables empathetic, multi-turn conversations and generates a summary of the chat for reflection.

The application includes secure authentication and session-based memory so users can interact seamlessly without permanent data storage.

✨ Features
🔐 Authentication System
Login
Signup
Continue as Guest
Logout

🧠 Multi-Turn Conversation
Context-aware responses
Session-based chat history
Real-time interaction

📝 Chat Summary
AI-generated conversation summary
Helps users reflect on their thoughts and feelings

🔒 Privacy Focused
No permanent database storage
Data resets on page refresh

Tech Stack
Frontend & App Framework: Streamlit
LLM: Gemini 2.5 Flash
Backend Logic: Python
Session Management: Streamlit Session State
Authentication: Custom auth module

🧠 app.py — Main App
Streamlit UI & navigation
Login / Signup / Guest flow
Session state & chat history
Chat interface + summary display
Connects frontend with backend
Entry point of the application

🤖 api.py — Gemini Chat Engine
Handle multi-turn conversation
Send/receive messages
Generate AI responses & chat summary

🔐 auth.py — Authentication
Login / Signup / Guest session
Logout handling
Auth state management
Success & error messages

🧾 prompt.py — AI Behavior
System prompt
Empathetic & supportive tone
Mental health safety guidelines

📦 requirements.txt — Dependencies
Project libraries (Streamlit, Gemini SDK, etc.)
Quick environment setup

⚙️ config.py — App configuration
API key & model settings
Global constants

How It Works
User selects:
Login / Signup / Guest
Session state is created
Multi-turn conversation begins
Chat history stored temporarily
AI generates summary on request


AWS EC2 Deployment Guide
Launch an EC2 Instance on Amazon Web Services
Choose Ubuntu Server
Instance type: t3.micro (free tier eligible)
Add Security Group
Connect to EC2
Update the system - sudo apt update && sudo apt upgrade 
Install Python & required tools -sudo apt install python3-pip python3
Upload project from local machine
Navigate to project folder -cd mental-health-chatbot
Create virtual environment -python3 -m venv venv -source venv/bin/activate
Install dependencies -pip install -r requirements.txt
Add Streamlit secrets (API key) -nano .env [Open the terminal and add your API key using the Streamlit secrets configuration. Use the EC2 terminal to securely configure the API key in the secrets.toml file.]
Run the Streamlit app -nohup streamlit run app.py
