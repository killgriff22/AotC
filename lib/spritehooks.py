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
    class Sprite:
        def __init__(self, _name:str, _posx:int, _posy:int,_costumelist:list,_spritefunc,_clonedata=None,_usesevents=False,_eventfunc=None):
            if not _clonedata:
                self.isclone=False
                self.clonecount = 0
                self.cloneid= 0
                self.name = _name
                self.pos = (_posx, _posy)
                self.costumelist = _costumelist
                self.currentcostume = self.costumelist[0]
                self.spritefunc = _spritefunc
                self.eventfunc = _eventfunc
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
                        self.currentcostume,
                        self.costumelist,
                        self.spritefunc
                    ]
                ]
        def get_object(self): return self.exports
        def change_costume(t1,costume:str,costumelist:list):
            print(type(costume))
            t1.exports[1][5] = costumelist[costumelist.index(costume)]
            return t1
        def register_Clone(t1,spritelist):
            t1.exports[1][4] = t1.clonecount + 1
            t1.clonecount = t1.clonecount + 1
            clone = Sprite(t1.name,t1.pos[0]+128,t1.pos[1],t1.costumelist,t1.spritefunc,(t1.clonecount,t1.clonecount,t1.costumelist[1]))
            spritelist.append(clone.get_object())
            return spritelist
        
else:
    import os
    os.system("python3 main.py")
    exit