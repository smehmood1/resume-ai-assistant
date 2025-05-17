import os
from flask import Flask, request, render_template
from PyPDF2 import PdfReader
import docx
from dotenv import load_dotenv
import openai
from openai import OpenAIError, RateLimitError, AuthenticationError

# Initialize Flask app
app = Flask(__name__)

UPLOAD_FOLDER = "./uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Make sure upload folder exists

# Load API key from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.organization = "org-SxWSRgsGpIGvD1A2krMSzGB5"

def extract_text_from_pdf(path):
    text = ""
    with open(path, "rb") as f:
        pdf = PdfReader(f)
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

def extract_text_from_docx(path):
    doc = docx.Document(path)
    full_text = [para.text for para in doc.paragraphs]
    return "\n".join(full_text)

def get_ai_feedback(text):
    prompt = f"Give feedback on this resume text:\n\n{text}"

    try:
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
            max_tokens=200,
            temperature=0.7,
        )
        return response.choices[0].message.content

    except RateLimitError:
        return "⚠️ OpenAI quota exceeded. Please upgrade your account to receive feedback."
    except AuthenticationError:
        return "❌ Invalid API key. Please check your OpenAI API key in the .env file."
    except OpenAIError as e:
        return f"🚨 An OpenAI error occurred: {str(e)}"

@app.route("/", methods=["GET", "POST"])
def upload_resume():
    if request.method == "POST":
        uploaded_file = request.files.get("resume")
        if uploaded_file:
            filepath = os.path.join(UPLOAD_FOLDER, uploaded_file.filename)
            uploaded_file.save(filepath)

            ext = uploaded_file.filename.lower().split('.')[-1]
            if ext == "pdf":
                text = extract_text_from_pdf(filepath)
            elif ext == "docx":
                text = extract_text_from_docx(filepath)
            else:
                return "Unsupported file type. Please upload PDF or DOCX.", 400

            ai_feedback = get_ai_feedback(text)

            # Use results.html template here
            return render_template("results.html",
                                   extracted_text=text[:500],
                                   feedback=ai_feedback)

        return "No file uploaded", 400

    # Use index.html template here
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
