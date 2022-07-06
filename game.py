if not __name__ == "__main__":
    import pygame,asyncio
    from lib import spritehooks as sphk
    def testsprite(sprite):print(f"i am a sprite and i have {sprite[1][4]} clones of my self and i am clone # {sprite[1][3]}")
    sprite = sphk.Sprite("test1",0,0,["./rec/testimg.png","./rec/sprite_test0.png"],testsprite)
    sprites = [sprite.get_object()]
    sprites = sprite.register_Clone(sprites)
    sprite.change_costume("./rec/sprite_test0.png",sprite.costumelist)  
else:
    import os
    os.system("python3 main.py")
    exit