def validate_link_youtube(link: str) -> bool:
    if not link.startswith("https://www.youtube.com") and not link.startswith(
        "https://youtu.be"
    ):
        return False
    return True
