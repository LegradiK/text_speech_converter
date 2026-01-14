import os
from dotenv import load_dotenv
from pathlib import Path
from pypdf import PdfReader
from flask import Flask, render_template, request, session, jsonify

load_dotenv(dotenv_path=Path(__file__).parent / "data.env")

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY')

speech_file_path = Path(__file__).parent / "speech.mp3"

reader = PdfReader("Annabel_Lee_Edgar_Allan_Poe.pdf")
text = ""
for page in reader.pages:
    text += page.extract_text() + "\n"

extracted_text = text.strip()
# print(extracted_text)

@app.route("/")
def home():
    return render_template("home.html", text=extracted_text, speech_file=str(speech_file_path))

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

if __name__ == "__main__":
    app.run(debug=True)

