from pathlib import Path
from pypdf import PdfReader
from flask import Flask, render_template

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=True)

