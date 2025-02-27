import streamlit as st
from utils.validators import validate_link_youtube
from formater.gemini import transform_transcrip_to_text


def main():

    st.title("Enter the link of the video you want to download")
    link = st.text_input("Enter the link here")
    if not link:
        st.warning("Please enter a link")
        return
    if not validate_link_youtube(link, st):
        st.warning("Please enter a valid YouTube link")
        return

    with st.spinner("Transcribing..."):
        response = transform_transcrip_to_text(link=link)

        st.subheader("Transcription:")
        st.code(response)


if __name__ == "__main__":
    main()
