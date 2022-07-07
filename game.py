if not __name__ == "__main__":
    import pygame,asyncio
    from lib import spritehooks as sphk
    def testsprite(spritedata):
        if spritedata[0][8]:
            print(f"i am a sprite and i have {spritedata[0][4]} clones of my self and i am clone # {spritedata[0][3]} and i am a clone")
        else:
            print(f"i am a sprite and i have {spritedata[0][4]} clones of my self and i am clone # {spritedata[0][3]} and i am not a clone")
    sprite = sphk.Sprite("test1",0,0,["./rec/testimg.png","./rec/sprite_test0.png"],testsprite)
    sprites = [sprite.get_object()]
    for i in range(3):
        sprites, clone = sprite.register_Clone(sprites)
    sprite = sprite.change_costume("./rec/sprite_test0.png",sprite.costumelist)  
else:
    import os
    os.system("python3 main.py")
    exit