import streamlit as st
from pytube import YouTube
from pydub import AudioSegment
import os
AudioSegment.converter = "/path/to/ffmpeg" 
# Streamlit app title
st.title("YouTube to MP3 Downloader")

# Input field for YouTube URL
youtube_url = st.text_input("Enter the YouTube video URL:")

# Function to download and convert YouTube video to MP3
def download_mp3(url):
    try:
        # Fetch the YouTube video
        yt = YouTube(url)
        st.write(f"Downloading: {yt.title}")

        # Get the highest quality audio stream
        audio_stream = yt.streams.filter(only_audio=True).first()

        # Download the audio stream
        audio_file = audio_stream.download(output_path="downloads")

        # Convert the downloaded file to MP3 using pydub
        mp3_file = os.path.splitext(audio_file)[0] + ".mp3"
        audio = AudioSegment.from_file(audio_file)
        audio.export(mp3_file, format="mp3")

        # Remove the original downloaded file
        os.remove(audio_file)

        st.success("Download and conversion complete!")
        return mp3_file

    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None

# Download button
if st.button("Download MP3"):
    if youtube_url:
        mp3_file = download_mp3(youtube_url)
        if mp3_file:
            # Provide a download link for the MP3 file
            with open(mp3_file, "rb") as file:
                st.download_button(
                    label="Download MP3",
                    data=file,
                    file_name=os.path.basename(mp3_file),
                    mime="audio/mpeg"
                )
            # Clean up the MP3 file after download
            os.remove(mp3_file)
    else:
        st.warning("Please enter a valid YouTube URL.")
