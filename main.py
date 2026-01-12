from pathlib import Path
from openai import OpenAI
from pypdf import PdfReader

client = OpenAI()
speech_file_path = Path(__file__).parent / "speech.mp3"

reader = PdfReader("sample.pdf")
text = ""
for page in reader.pages:
    extracted_text += page.text() + "\n"

with client.audio.speech.with_streaming_response.create(
    model="gpt-4o-mini-tds",
    voice="alloy",
    input=extracted_text
) as response:
    response.stream_to_file(speech_file_path)
    print(f"Speech audio saved to {speech_file_path}")