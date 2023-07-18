import pyautogui
import time
from numpy import *
import mouseinfo
from PIL import ImageGrab, ImageOps

dino_coord = (134, 646)
restart_coord = (958, 576)

def restart():
    pyautogui.click(restart_coord)
    print("Restarting")

def detect_obstacle():
    box = (dino_coord[0]+55, dino_coord[1], dino_coord[0]+300   , dino_coord[1]+10)
    pixels = ImageGrab.grab(box)
    gray_scale = ImageOps.grayscale(pixels)
    get_colors = array(gray_scale.getcolors())
    #print(get_colors)
    print(get_colors.sum())
    return get_colors.sum()


def main():

    pyautogui.FAILSAFE = True
    #mouseinfo.MouseInfoWindow()    # Shows mouse coordinates

    time.sleep(4)   # Allows you to open the game window
    restart()

    game_on = True
    while game_on:
        detect_obstacle()
        if detect_obstacle() > 2705:
            pyautogui.keyDown('space')
            pyautogui.keyUp('space')
        if detect_obstacle() == 2714:
            game_on = False

if __name__ == '__main__':
    main()