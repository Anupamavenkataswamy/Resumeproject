from flask import Flask, render_template, request, send_from_directory
import os
import pdfminer.high_level
from docx import Document
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def extract_text(file_path):
    """Extract text from PDF or DOCX files."""
    if file_path.endswith('.pdf'):
        return pdfminer.high_level.extract_text(file_path)
    elif file_path.endswith('.docx'):
        doc = Document(file_path)
        return '\n'.join([para.text for para in doc.paragraphs])
    return ""

def extract_candidate_details(text):
    """Extract candidate's name, email, and phone number from resume."""
    name_match = re.search(r'Name[:\s]*([\w\s]+)', text, re.IGNORECASE)
    email_match = re.search(r'[\w\.-]+@[\w\.-]+', text)
    phone_match = re.search(r'\b\d{10}\b', text)

    name = name_match.group(1) if name_match else "Not Found"
    email = email_match.group(0) if email_match else "Not Found"
    phone = phone_match.group(0) if phone_match else "Not Found"

    return name.strip(), email, phone

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_files():
    """Upload multiple resumes and match them with job description."""
    
    job_description = request.form['job_description']
    
    if 'resumes' not in request.files:
        return "No files uploaded!"
    
    files = request.files.getlist('resumes')

    if not files or all(file.filename == '' for file in files):
        return "No selected files!"

    results = []

    for file in files:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        resume_text = extract_text(file_path)
        name, email, phone = extract_candidate_details(resume_text)

        # Compare resume with JD
        vectorizer = TfidfVectorizer()
        vectors = vectorizer.fit_transform([resume_text, job_description])
        similarity_score = cosine_similarity(vectors[0], vectors[1])[0][0] * 100

        results.append({
            "name": name,
            "email": email,
            "phone": phone,
            "score": round(similarity_score, 2),
            "file_name": file.filename
        })

    # Sort results by highest match percentage
    sorted_results = sorted(results, key=lambda x: x['score'], reverse=True)

    return render_template('results.html', results=sorted_results)

@app.route('/view/<filename>')
def view_file(filename):
    """View resumes in the browser instead of downloading."""
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
