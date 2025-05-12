# 🎧 Smart Audio Textbooks

> Turn textbook pages into bite-sized audio lessons in your preferred language.

Smart Audio Textbooks is a Streamlit-based app that converts textbook content (PDF or image) into translated audio. This is especially helpful for visually impaired users, language learners, or students seeking audio-based revision tools.

---

## 🚀 Features

- 📄 Upload textbook pages (images or PDFs)
- 🧠 OCR-based text extraction
- 🧹 Smart text sanitization
- ✂️ Text chunking for natural flow
- 🌍 Translation to regional Indian languages
- 🔊 Audio generation using Google Text-to-Speech (gTTS)
- 🎧 In-app audio playback

---

## 🛠 Tech Stack

| Layer             | Tech/Library                     |
|------------------|----------------------------------|
| Frontend         | [Streamlit](https://streamlit.io/)             |
| OCR              | [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) via `pytesseract` |
| PDF to Image     | `pdf2image`, [Poppler](https://github.com/oschwartz10612/poppler-windows/releases/) |
| Text Processing  | `nltk`, `re`, `langdetect`        |
| Translation      | `googletrans==4.0.0-rc1`         |
| Text-to-Speech   | `gTTS`                           |
| Image Handling   | `Pillow`                         |

---

## 📦 Project Structure

```plaintext
SmartBooktoAudioConverter/
│
├── app.py                     # Main Streamlit App
├── requirements.txt
├── audio_output/              # Stores generated audio files
├── utils/
│   ├── ocr.py                 # Extract text from image/pdf
│   ├── sanitizer.py           # Clean and sanitize text
│   ├── chunker.py             # Chunk long texts
│   ├── translator.py          # Translate chunks
│   └── texttovoice.py         # Convert chunks to audio

```

---

## ⚙️ Setup Guide

### ✅ Prerequisites

- Python 3.8+
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) (must be installed and added to PATH)
- [Poppler for Windows](https://github.com/oschwartz10612/poppler-windows/releases/) (required by `pdf2image`)

---


# Setup Guide
```bash
# Clone the Gitrepo
git clone https://github.com/yourusername/Smart-Audio-Textbooks.git
cd Smart-Audio-Textbooks

# Create the Virtual Enviroment and activte it
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

# install the requirements
pip install -r requirements.txt

# add nltk packages
python
import nltk
>>> nltk.download('punkt')
>>> nltk.download('punkt-tab')

# run the app
streamlit run app.py
```
