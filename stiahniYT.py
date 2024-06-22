import yt_dlp as youtube_dl
import os
import shutil
import tempfile


def download_audio(url, output_dir):
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as tmpdirname:
        ydl_opts = {
            'format': 'bestaudio/best',  # Download the best audio quality available
            'outtmpl': os.path.join(tmpdirname, '%(title)s.%(ext)s'),  # Use temporary directory
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',  # You can choose 'mp3', 'wav', 'm4a', etc.
                'preferredquality': '192',  # Audio quality (192 kbps for mp3)
            }],
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        # Move the downloaded file to the final output directory
        for filename in os.listdir(tmpdirname):
            shutil.move(os.path.join(tmpdirname, filename), output_dir)



video_url = 'https://www.youtube.com/watch?v=URHZSttbje4'
output_path = 'data/bilingual.mp4'  # Customize the output filename

download_audio(video_url, output_path)