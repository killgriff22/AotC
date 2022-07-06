import pygame
WIDTH = 360
HEIGHT = 480
FPS = 30
pygame.init()
pygame.mixer.init()
import game
sprites = game.sprites
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AttackoftheClones -- ENGINE DEMO")
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255,255,255))
    for name,pos,img in sprites:
        img = pygame.transform.scale(img,(128,128))
        screen.blit(img,pos)
    pygame.display.update()
pygame.quit()