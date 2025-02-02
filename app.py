# -*- coding: utf-8 -*-
"""app.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1BNwMETNGiTOnZtfqIRI5h61dY182ci8K
"""

import streamlit as st

# Import the download function
from download_youtube import download_youtube_video_to_mp3  # Ensure this matches your file name

def main():
    st.title("YouTube MP3 Downloader")
    st.write("Enter the YouTube video URL below to download it as an MP3 file.")

    video_url = st.text_input("YouTube Video URL")

    if st.button("Download"):
        if video_url:
            result = download_youtube_video_to_mp3(video_url)
            st.success(result)
        else:
            st.error("Please enter a valid YouTube video URL.")

if __name__ == "__main__":
    main()

