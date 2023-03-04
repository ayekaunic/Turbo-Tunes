# importing required libraries
from pytube import YouTube
import os
import subprocess

temp_folder_path = "C:/Users/CC/Music/temp/"
music_folder_path = "C:/Users/CC/Music/"

# prompting the user to enter the number of songs they want to download, then prompting them to enter the link and name for each song, storing the links and names in separate lists.
no_of_songs = int(input("How many songs to you want to download? "))
speed = input("What speed do you want to download them at? ")
print("\n")

links = []
names = []

for i in range(no_of_songs):
    link = input(f"Paste the link of the song no.{i+1}: ")
    name = input(f"Enter the name of the song no.{i+1}: ") + ".mp3"
    links.append(link)
    names.append(name)

# downloading the audio streams of the songs and saving them as audio files with their specified names in a temporary directory
for i in range(no_of_songs):
    url = links[i]
    
    try:
        yt = YouTube(url)
        audio = yt.streams.filter(only_audio=True).first()
        
        output_file = names[i]
        audio.download(output_path=temp_folder_path, filename=output_file)
    except: print(f"Couldn't download {names[i]}")
    
print("Songs downloaded! Speeding them up!")

# using fmpeg to speed up the songs and save the results to the music directory
for file_name in os.listdir(temp_folder_path):
    if file_name.endswith('.mp3'):
        input_path = os.path.join(temp_folder_path, file_name)
        output_path = os.path.join(music_folder_path, file_name)
        try:
            cmd = ['ffmpeg', '-i', input_path, '-filter:a', f'atempo={speed}', output_path]
            subprocess.run(cmd, check=True)
        except: print(f"Couldn't speed up {file_name}")
        
print("Songs sped up! Deleting temporary files...")

# deleting all the files in the temporary directory 
for filename in os.listdir(temp_folder_path):
    file_path = os.path.join(temp_folder_path, filename)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
    except Exception as e:
        print(f"Error deleting file: {file_path} - {e}")
        
print("Temporary files deleted! All done!")