import streamlit as st
from utils.ocr import extract_text_from_image, extract_text_from_pdf
from utils.sanitizer import sanitize_text
from utils.chunker import chunk_text
from utils.translator import translate_chunks
from utils.texttovoice import convert_chunk_to_audio
import io

LANGUAGE_CODES = {
    "English": "en",
    "Hindi": "hi",
    "Marathi": "mr",
    "Gujarati": "gu",
    "Tamil": "ta",
    "Telugu": "te",
    "Bengali": "bn",
    "Punjabi": "pa",
    "Urdu": "ur",
    "Kannada": "kn",
    "Malayalam": "ml",
    "Odia": "or",
    "Assamese": "as",
    "Nepali": "ne",
    "Sanskrit": "sa",
}

# Page Config
st.set_page_config(page_title="Smart Audio Book", layout="centered")


# Title of the Page
st.title("Smart Audio Textbooks")
st.subheader("Turn textbook pages into bite-sized audio lessons in your language.")


# File upload
uploaded_file = st.file_uploader(
    "Upload a textbook page (image or PDF)",
    type=["png", "jpg", "jpeg", "pdf"]
)


# Language selection
languages = list(LANGUAGE_CODES.keys())
selected_language = st.selectbox("Select target language", languages)


def process_file(uploaded_file):

    if uploaded_file.type in ["image/png", "image/jpeg", "image/jpg"]:

        # Extracting text from image
        text = extract_text_from_image(uploaded_file)
    elif uploaded_file.type == "application/pdf":

        # Extacting text from pdf
        text = extract_text_from_pdf(uploaded_file)
    else :
        text = "Unsupported File Formate"
    
    return text




progress_text = st.empty()

text = "" # text string
# Submit button
if st.button("🎧 Generate Audio"):
    if uploaded_file is None:
        st.warning("Please upload a textbook page.")
    else:
        with st.spinner("Processing..."):
            text = process_file(uploaded_file)
            text = sanitize_text(text) # Sanitizing text

            # converting text into chunks
            chunks = chunk_text(text)
            progress_text.text("✅ Chunks Created!")



            # translating Chunks to selected language
            translated_chunks = translate_chunks(chunks=chunks, target_lang=LANGUAGE_CODES[selected_language])
            progress_text.text("✅ Translation Completed")
            progress_text.text("✅ Starting Audio Conversion!")
            try :
                

                    for i, chunk in enumerate(translated_chunks):
                        progress_text.text(f"✅ Audio File {i+1} ")
                        progress_text.text(f"Processing chunk {i+1}/{len(translated_chunks)}")
                        filename = f"audio_output/chunk_{i+1}.mp3"

                        convert_chunk_to_audio(chunk, lang_code=LANGUAGE_CODES[selected_language], filename=filename)
                        
                        with open(filename, "rb") as audio_file:
                            audio_bytes = audio_file.read()
                            st.audio(audio_bytes, format="audio/mp3")
                    


                    progress_text.text("✅ All chunks processed!")



            except Exception as e:
                print(f"Error converting text to audio: {e}")
           
                