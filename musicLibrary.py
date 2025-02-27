music={
    "delicate": "https://youtu.be/tCXGJQYZ9JA",
    "die":"https://youtu.be/jFJ11i0Q2oE",
    "attention":"https://youtu.be/nfs8NYg7yQM"
}

# music.py
import os
import random
import pygame


def play_music(file):
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def get_music_files(directory):
    music_files = []
    for file in os.listdir(directory):
        if file.endswith(".mp3"):
            music_files.append(os.path.join(directory, file))
    return music_files

def play_random_music(music_files):
    selected_song = random.choice(music_files)
    print(f"Playing: {os.path.basename(selected_song)}")
    play_music(selected_song)







