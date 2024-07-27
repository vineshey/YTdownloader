import yt_dlp
import sys

def download_video(url):
    ydl_opts = {
        'outtmpl': 'C:/Users/ACER/Downloads/%(title)s.%(ext)s',
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download completed!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        download_video(sys.argv[1])
    else:
        print("Please provide a YouTube URL.")
