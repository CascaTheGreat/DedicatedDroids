from os import listdir
from playsound import playsound
from random import choice
files = listdir("voicelines")

def play_random():
    file = choice(files)
    playsound("voicelines/" + file)