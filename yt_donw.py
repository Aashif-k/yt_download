from pytube import YouTube
from pydub import AudioSegment
import streamlit as st
import os

def yt_down(video_url):
    link=st.text_input(" ",placeholder="enter the url of the video")
    try:
        # Create YouTube object
        yt = YouTube(video_url)

        # Get the highest resolution stream
        video_stream = yt.streams.filter(only_audio=True).first()

        # Download the video
        print(f'Downloading: {yt.title}')
        video_file = video_stream.download(filename='temp_video')

        # Convert video to audio
        audio_file = 'output_audio.mp3'
        audio = AudioSegment.from_file(video_file)
        audio.export(audio_file, format='mp3')

        # Clean up temporary video file
        os.remove(video_file)

        print(f'Conversion complete! Saved as: {audio_file}')
    except Exception as e:
        print(f'Error: {e}')
def main():
    yt_down(link)
if __name__=='__main__':
  main()
