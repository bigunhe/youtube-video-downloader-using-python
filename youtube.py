import yt_dlp
import tkinter as tk
from tkinter import filedialog
import os


root = tk.Tk()
root.withdraw()


def download_video(url, save_path):
    try:
        # yt-dlp options: download best quality MP4, save to selected path
        ydl_opts = {
            "outtmpl": os.path.join(
                save_path, "%(title)s.%(ext)s"
            ),  # filename template
            "format": "best[ext=mp4]/best",  # prefer MP4, fallback to best
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            print("Video Downloaded Successfully!")
    except Exception as e:
        print(e)


# sample url = "https://www.youtube.com/shorts/_SES9ESP0_o"

url = input("Enter the youtube URL you want to download")
save_path = filedialog.askdirectory(title="Select Download Folder")

if save_path:
    download_video(url, save_path)
else:
    print("No folder selected. Download cancelled")
