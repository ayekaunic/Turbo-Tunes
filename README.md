# Turbo Tunes
This program allows you to download songs from YouTube and speed them up before saving them to your computer. It uses the **PyTube** library to download audio streams from YouTube, and the **FFmpeg** library to speed up the songs.

## Prerequisites
Before you can use this program, you need to have the following software installed on your computer:

- Python 3
- PyTube
- FFmpeg

You can install PyTube using pip, the Python package manager. Run the following command:

```pip install pytube```

To install FFmpeg, follow the instructions for your operating system on [the official FFmpeg website](https://ffmpeg.org/).

## Usage
To use this program, simply run the **main.py** file in Python. You will be prompted to enter the number of songs you want to download, as well as the speed at which you want to download them. You will then be prompted to enter the link and name for each song.

The downloaded songs will be saved as MP3 files in a temporary folder (C:/Users/CC/Music/temp/ by default). They will then be sped up by the specified amount using FFmpeg, and saved as MP3 files in a music folder (C:/Users/CC/Music/ by default).

After the songs have been downloaded and sped up, the program will delete all the files in the temporary folder.
