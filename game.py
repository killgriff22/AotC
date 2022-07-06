if not __name__ == "__main__":
    import pygame
    from lib import spritehooks as sphk
    sprites = [sphk.Sprite("test1",0,0,["./rec/testimg.png"]).get_object()]
else:
    import os
    os.system("python3 main.py")
    exit