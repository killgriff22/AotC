import pygame,os
WIDTH = 360
HEIGHT = 480
FPS = 30
pygame.init()
pygame.mixer.init()
import game,asyncio
sprites = game.sprites
screen = pygame.display.set_mode((WIDTH, HEIGHT))
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
    screen.fill((255,255,255))
    for sprite in sprites:
        name, pos, img, func = sprite[0]
        func(sprite)
        img = pygame.transform.scale(img,((WIDTH-img.get_width())/RESIZE,(HEIGHT-img.get_height())/RESIZE))
        screen.blit(img,pos)
    print(frame)
    pygame.display.update()
pygame.quit()