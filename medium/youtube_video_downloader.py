from pytube import YouTube
import tkinter as tk
from tkinter import filedialog


def download_video(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        highest_res_stream = streams.get_highest_resolution()
        highest_res_stream.download(output_path=save_path)
        print("Video downloaded successfully!")

    except Exception as e:
        print(e)


def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")

    return folder


# Makes sure this particular file is being directly run before running the code
# This stops other programs referencing this file from running the code
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    video_url = input("Enter a YouTube video URL: ")
    save_dir = open_file_dialog()

    if not save_dir:
        print("Invalid save directory.")
    else:
        print("Downloading video...")
        download_video(video_url, save_dir)
