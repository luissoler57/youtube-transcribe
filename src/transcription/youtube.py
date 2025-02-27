from youtube_transcript_api import YouTubeTranscriptApi
from typing import Optional


def download_video(link: str) -> str:
    video_id = link.split("v=")[1]
    lineas = ""
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=["es"])
        for line in transcript:
            lineas += line["text"] + "\n"
        return lineas

    except YouTubeTranscriptApi.CouldNotRetrieveTranscript as e:
        return f"Could not retrieve transcript: {e}"
    except YouTubeTranscriptApi.NoTranscriptFound as e:
        return f"No transcript found: {e}"
