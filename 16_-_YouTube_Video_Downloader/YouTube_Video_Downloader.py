from pytube import YouTube
import tkinter as tk
from tkinter import filedialog


def download_video(url, save_path):
    try:
        # Attempt to create a YouTube object
        yt = YouTube(url)

        # Filter streams to get the highest resolution progressive MP4 stream
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        highest_res_stream = streams.get_highest_resolution()

        # Download the video to the specified save path
        highest_res_stream.download(output_path=save_path)
        print("Video downloaded successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")


def open_file_dialog():
    # Open a file dialog to choose a directory for saving the video
    root = tk.Tk()
    root.withdraw()
    folder = filedialog.askdirectory()

    if folder:
        print(f"Selected Folder: {folder}")
    return folder


def main():
    print("Welcome to YouTube Video Downloader!")

    # Prompt user for YouTube video URL
    video_url = input("Please enter a YouTube URL: ")

    # Open file dialog to select save directory
    save_dir = open_file_dialog()

    if save_dir:
        print("Starting download...")
        download_video(video_url, save_dir)
    else:
        print("No save location selected. Download aborted.")


if __name__ == "__main__":
    main()
