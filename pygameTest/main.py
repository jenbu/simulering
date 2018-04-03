import pygame, matplotlib, math, numpy
from functions import *


SCREENWIDTH = 600
SCREENHEIGHT = 480
BLACK = (0,0,0)

screen = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))

pygame.init()
myFont = pygame.font.SysFont("monospace", 15)

running = True
counter = 0


def draw():
    screen.fill((255,255,255))
    pulley = pygame.draw.circle(screen, (0,0, 0), (100, 100), int(pRadius*10), 2)
    drum = pygame.draw.circle(screen, BLACK, (pulley[0]+pulley[2]+drumRadius, 200), drumRadius, 1)
    pygame.draw.line(screen, (128,128,128),(pulley[0]+pulley[2]/2, pulley[1]+pulley[3]/2), (pulley[0]+pulley[2]/2+10*pRadius*math.cos(theta), pulley[1]+pulley[3]/2+10*pRadius*math.sin(theta)))

    mass1 = pygame.draw.rect(screen, (0,0,128), (pulley[0]-32/2, -y+SCREENHEIGHT-100, 32,16))
    pygame.draw.line(screen, (0,0,0), (pulley[0], pulley[1]+ pulley[3]/2), (mass1[0]+mass1[2]/2, mass1[1]+ mass1[3]/2))
    label = myFont.render(str(time), 1, (0,0,0))
    screen.blit(label, (SCREENWIDTH-70, 50))
    pygame.display.update()


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    if time <= timeEnd:
        y, yDot, theta, thetaDot, time = calculation(y, yDot, theta, thetaDot, time)
    draw()




