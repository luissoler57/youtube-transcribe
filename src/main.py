import streamlit as st
from downloader.youtube import download_video


def main():

    st.title("Enter the link of the video you want to download")
    link = st.text_input("Enter the link here")
    if not link:
        st.warning("Please enter a link")
        return
    if st.button("Transcribe"):
        st.write("Transcript:")

        transcript = download_video(link)
        st.write(transcript)


if __name__ == "__main__":
    main()
