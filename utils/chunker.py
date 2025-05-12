from nltk.tokenize import sent_tokenize


def chunk_text(text, max_words=400):
    """
    Splits sanitized text into chunks of approximately max_words length.
    
    Args:
        text (str): The input sanitized text.
        max_words (int): Maximum words per chunk (default is 400).
    
    Returns:
        List[str]: A list of text chunks.
    """
    sentences = sent_tokenize(text)
    chunks = []
    current_chunk = ""

    for sentence in sentences:
        if len((current_chunk + " " + sentence).split()) <= max_words:
            current_chunk += " " + sentence
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence

    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks
