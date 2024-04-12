#-------------------------------------------------------------------------------------#
# Author: Shama.T.S
# Project Name : Import Audio File using Python
# Version : 1.1
# Date : 12-04-2024
# To Do : install pygame: pip install pygame
#-------------------------------------------------------------------------------------#
import pygame
import time 

def play_music():
    pygame.init()
    file_path = "D:\Python\project3\sound\sound1.mp3"
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

play_music()
time.sleep(25)
print("Thanks for listening!!")