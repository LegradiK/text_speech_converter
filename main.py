import os
from dotenv import load_dotenv
from pathlib import Path
from pypdf import PdfReader
from flask import Flask, flash, render_template, request, session, jsonify, redirect, url_for


load_dotenv(dotenv_path=Path(__file__).parent / "data.env")

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY')

def extract_pdf_text(file):
    file.seek(0)
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"

    extracted_text = text.strip()

    return extracted_text
    # print(extracted_text)

@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files.get("pdf_file")

    if not file:
        flash ("No file selected")
        return redirect(url_for("home"))
    if not file.filename.lower().endswith(".pdf"):
        flash ("Invalid file type. Please upload a PDF file.")
        return redirect(url_for("home"))

    filename = file.filename
    extracted_text = extract_pdf_text(file)

    return render_template(
        "home.html",
        extracted_text=extracted_text,
        pdf_file_name=filename
    )

@app.route('/favicon.ico')
def favicon():
    return '', 204

@app.route('/puter-login', methods=['POST'])
def puter_login():
    data = request.get_json()

    session['user'] = {
        'username': data['username'],
        'provider': 'puter'
    }

    return jsonify({'success': True})

@app.route('/puter-logout', methods=['POST'])
def puter_logout():
    session.pop('user', None)
    return jsonify({'success': True})

if __name__ == "__main__":
    app.run(debug=True)

