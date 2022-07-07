import pygame,os
WIDTH = 360
HEIGHT = 480
FPS = 30
pygame.init()
pygame.mixer.init()
import game,asyncio
sprites = game.sprites
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("AttackoftheClones -- ENGINE DEMO")
clock = pygame.time.Clock()
running = True
RESIZE = 2.5
frame = 0
while running:
    clock.tick(FPS)
    if not frame < 60:frame = 0
    else: frame += 1
    os.system('clear')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            WIDTH = event.w
            HEIGHT = event.h
    screen.fill((255,255,255))
    clonecount = 0
    for sprite in sprites:
        name, pos, img, cloneid,clonecount,currentcostume,costumelist, func, isclone,obj = sprite[0]
        func(sprite)
        img = pygame.transform.scale(img,((WIDTH-img.get_width())/RESIZE,(HEIGHT-img.get_height())/RESIZE))
        screen.blit(img,(pos[0]+img.get_width()*cloneid,pos[1]))
    print(f"MASTER - {clonecount} CLONES | FRAME - {frame} | FPS - {clock.get_fps()} | SIZE - {WIDTH}X{HEIGHT}")
    pygame.display.update()
pygame.quit()