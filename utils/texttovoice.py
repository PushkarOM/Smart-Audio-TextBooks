from gtts import gTTS
# import os
# os.makedirs("audio_output", exist_ok=True)

def convert_chunk_to_audio(text_chunk: str, lang_code: str, filename: str):
    
    try:
        from gtts import gTTS
        tts = gTTS(text_chunk, lang=lang_code)
        tts.save(filename)
        return True
    
    except Exception as e:
        print(f"[Error] gTTS failed: {e}")
        return False



    
    