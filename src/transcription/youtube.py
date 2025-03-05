from youtube_transcript_api import (
    CouldNotRetrieveTranscript,
    NoTranscriptFound,
    YouTubeTranscriptApi,
)


def download_transcription_video(link: str) -> str:
    video_id = link.split("v=")[1]
    lineas = ""
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=["es"])
        for line in transcript:
            lineas += line["text"] + "\n"
        return lineas
    except CouldNotRetrieveTranscript as e:
        return f"Could not retrieve transcript: {e}"
    except NoTranscriptFound as e:
        return f"No transcript found: {e}"
