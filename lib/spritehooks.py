if not __name__ == "__main__":
    import pygame
    pygame.init()
    ALL_SPRITES_TO_DRAW = [None]
    class Sprite:
        def __init__(self, _name:str, _posx:int, _posy:int,_costumelist:list):
            self.name = _name
            self.pos = (_posx, _posy)
            self.costumelist = _costumelist
            self.currentcostume = self.costumelist[0]
            self.exports = [self.name,self.pos,pygame.image.load(self.currentcostume)]
        def get_object(self): return self.exports
        def change_costume(costume:str):0
else:
    import os
    os.system("python3 main.py")
    exit