# translator_tool.py
from deep_translator import GoogleTranslator

def translate_to_german(text: str):
    """
    Translate English text to German using deep-translator.
    """
    if not text.strip():
        return "No text to translate."
    try:
        translated = GoogleTranslator(source='en', target='de').translate(text)
        return translated
    except Exception as e:
        return f"Translation error: {e}"