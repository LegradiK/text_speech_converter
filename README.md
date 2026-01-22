# PDF Text Reading App

This is a web application that allows users to read PDF files and convert their text to speech using selectable languages and voices. The app integrates Puter AI for text-to-speech functionality and supports multiple languages.

A <a href="https://puter.com/">Puter</a> account is required to use this application.

## Features

- Upload and read PDF files.
- Automatic language detection for PDFs.
- Selectable voices per language.
- Play, pause, and stop audio playback.
- User authentication using Puter Sign-in.
- Clear message for unsupported languages.
- Responsive and mobile-friendly design.

## Supported Languages

- English (GB / US)
- Japanese
- French
- German
- Italian
- Portuguese
- Spanish

*Unsupported languages display a message to inform the user.*

## Installation

1. Clone the repository:

```bash
git clone <your-repo-url>
cd pdf-text-reading-app
```

2. Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # Linux
```

3. Source a virtual environment:

```bash
source venv/bin/activate
```

4. Run*
```bash
python3 main.py
```

*install any dependencies if you don't have
<i>e.g.Flask, load_dotenv, PdfReader, Path, langdetect</i>

5. Access the app at http://127.0.0.1:5000.

## Usage

1. Sign in using the Puter sign-in button. Popup window will appear to prompt you to sign in.

2. Upload a PDF file.

3. If the language is supported:

4. Select the preferred language and voice.

5. Use the Play, Pause, and Stop buttons to control the audio.*

*If the language is unsupported, a message will appear, and audio controls will be disabled.

## License and Attribution

Icons used in this project are provided by Flaticon:
<a href="https://www.flaticon.com/free-icons/play" title="play icons">Play icons created by Freepik - Flaticon</a>
<a href="https://www.flaticon.com/free-icons/pause-button" title="pause button icons">Pause button icons created by inkubators - Flaticon</a>
<a href="https://www.flaticon.com/free-icons/stop-button" title="stop button icons">Stop button icons created by Pixel perfect - Flaticon</a>

## Dependencies

Flask
pdfplumber
langdetect
Puter AI JS SDK
Font Awesome (via CDN)