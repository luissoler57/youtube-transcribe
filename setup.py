from setuptools import find_packages, setup

setup(
    name="youtube-transcribe",
    version="0.1.0",
    description="YouTube transcription tool that downloads and processes video transcripts.",
    packages=find_packages(),
    install_requires=[
        "youtube-transcript-api",
        "google-genai",
        "pyperclip",
    ],
)
