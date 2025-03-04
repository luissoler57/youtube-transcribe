"""
Module for transforming YouTube video transcriptions to coherent text using Google Gemini AI.
"""

import os

# Third-party imports
from google import genai
from google.genai import types

# First-party imports
from src.transcription.youtube import download_video

API_GEMINI = os.environ.get("API_GEMINI")

client = genai.Client(api_key="AIzaSyCe1OMCHVLtIlUhk1C6iDkprBhAMCcW2U8")
MODEL_GEMINI = "gemini-2.0-flash"

SYS_INSTRUCT = (
    "Eres un especialista en el idioma espanol, "
    "al recibir un texto de una transcripcion, "
    "organizalo y un texto legible, con semantica y coherencia. "
    "Realiza un Glossario de terminos y una lista de referencias."
    "Valida la informacion para asegurar que sea correcta y relevante."
)


def transform_transcrip_to_text(link: str):
    """
    Transform a YouTube video transcript into a coherent text.

    Args:
        link: YouTube video URL

    Returns:
        Processed text from Gemini AI
    """
    transcript = download_video(link)

    response = client.models.generate_content(
        model=MODEL_GEMINI,
        config=types.GenerateContentConfig(system_instruction=SYS_INSTRUCT),
        contents=transcript,
    )

    return response.text
