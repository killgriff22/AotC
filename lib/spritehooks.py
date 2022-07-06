def count(lst, x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count
if not __name__ == "__main__":
    import pygame,asyncio
    import collections
    pygame.init()
    ALL_SPRITES_TO_DRAW = [None]
    class Sprite:
        def __init__(self, _name:str, _posx:int, _posy:int,_costumelist:list,_spritefunc,_clonedata=None):
            if not _clonedata:
                self.isclone=False
                self.clonecount = 0
                self.cloneid= 0
                self.name = _name
                self.pos = (_posx, _posy)
                self.costumelist = _costumelist
                self.currentcostume = self.costumelist[0]
                self.spritefunc = _spritefunc
                self.exports = [
                    [
                        self.name,
                        self.pos,
                        pygame.image.load(self.currentcostume),
                        self.spritefunc
                        ],
                    [
                        self.name,
                        self.pos,
                        pygame.image.load(self.currentcostume),
                        self.cloneid,
                        self.clonecount,
                        self.spritefunc
                    ]
                ]
            elif _clonedata:
                self.isclone=True
                self.clonecount = _clonedata[0]
                self.cloneid= _clonedata[1]
                self.name = _name
                self.pos = (_posx, _posy)
                self.costumelist = _costumelist
                self.currentcostume = _clonedata[2]
                self.spritefunc = _spritefunc
                self.exports = [
                    [
                        self.name,
                        self.pos,
                        pygame.image.load(self.currentcostume),
                        self.spritefunc
                        ],
                    [
                        self.name,
                        self.pos,
                        pygame.image.load(self.currentcostume),
                        self.cloneid,
                        self.clonecount,
                        self.spritefunc
                    ]
                ]
        def get_object(self): return self.exports
        def change_costume(costume:str,self):
            self.currentcostume = self.costumelist[self.costumelist.index(costume)]
            return self
        #register a clone as a new sprite using the same name and increase the clonecount
        def register_Clone(self,spritelist):
            self.clonecount = self.clonecount + 1
            clone = Sprite(self.name,self.pos[0],self.pos[1],self.costumelist,self.spritefunc,(self.clonecount,self.clonecount,self.currentcostume))
            spritelist.append(clone.get_object())
            return spritelist
        
else:
    import os
    os.system("python3 main.py")
    exit