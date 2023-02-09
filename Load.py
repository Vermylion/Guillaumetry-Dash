import pygame
import json

def settings():
    import LevelCreate

    #Open file
    f = open('Settings.json')
    #Transfer json data into readable python data
    data = json.load(f)

    #Set vars to settings in file
    LevelCreate.draw_collisions = data['Settings']['Show Collisions']

    #Close the file
    f.close()