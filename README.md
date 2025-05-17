# 🧠 Resume AI Assistant

An AI-powered web app that provides feedback on uploaded resumes using OpenAI's GPT model. Built with Flask, Python, and the OpenAI API.

## ✨ Features

- Upload resumes in **PDF** or **DOCX** format
- Extract and preview resume text
- Use **GPT-4o** to provide personalized AI feedback
- Simple and responsive web interface

## 🚀 How It Works

1. Upload your resume via the homepage.
2. The app extracts the text using PyPDF2 or python-docx.
3. Text is sent to OpenAI's API.
4. Feedback is generated and displayed on the page.

## 🛠 Tech Stack

- **Python**
- **Flask**
- **OpenAI API**
- **PyPDF2**, **python-docx**
- **python-dotenv** for environment variable management

## 🔐 Setup & Run Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/smehmood1/resume-ai-assistant.git
   cd resume-ai-assistant

2. Create a virtual environment and activate it:
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install dependencies:
    pip install -r requirements.txt

4. Create a .env file and add your OpenAI API key:
    OPENAI_API_KEY=your_openai_api_key_here

5. Run the app:
    python app.py

6. Visit http://127.0.0.1:5000/ in your browser.

📂 File Structure
resume-ai-assistant/
│
├── app.py              # Main Flask app
├── uploads/            # Resume upload folder
├── .env                # OpenAI API key (excluded in .gitignore)
├── .gitignore
├── requirements.txt
└── README.md

⚠️ Notes
.env and __pycache__/ are excluded from version control.
This app is for educational and portfolio purposes only.

📄 License
MIT License

Made by @smehmood1

