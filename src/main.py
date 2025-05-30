"""
YouTube transcription tool that downloads and processes video transcripts.

This module allows users to enter a YouTube link, download the transcript,
and format it into readable text.
"""

from formater.transcrition_video import transform_transcrip_to_text
from transcription.youtube import download_transcription_video
from utils.validators import validate_link_youtube


def main():
    """
    Main function that handles user input and processes YouTube transcriptions.
    Prompts the user for a YouTube link, validates it, downloads the transcript,
    and formats it into readable text.
    """

    print("Welcome to the YouTube transcription tool!")
    # Get input from the user
    link = input("Please enter the link to the youtube: ")
    while not validate_link_youtube(link):
        print("Please enter a valid youtube link!")
        link = input("Please enter the link to the youtube: ")

    transcript = download_transcription_video(link)
    gemini_complete = transform_transcrip_to_text(transcript=transcript)
    print(f"\n{gemini_complete}")


if __name__ == "__main__":
    main()
