# utils/translator.py
from googletrans import Translator

def translate_text(text, target_lang='hi'):
    """
    Translates a given text to the target language using Google Translate API.

    Args:
        text (str): Text to translate.
        target_lang (str): The target language code (e.g., 'hi' for Hindi, 'ta' for Tamil).

    Returns:
        str: Translated text.
    """
    translator = Translator()
    translated = translator.translate(text, dest=target_lang)
    return translated.text



def translate_chunks(chunks, target_lang='hi'):
    """
    Translates a list of text chunks into the target language.

    Args:
        chunks (List[str]): List of text chunks to translate.
        target_lang (str): The target language code.
    
    Returns:
        List[str]: List of translated text chunks.
    """
    translated_chunks = [translate_text(chunk, target_lang) for chunk in chunks]
    return translated_chunks
