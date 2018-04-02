import pygame, matplotlib, math, numpy

SCREENWIDTH = 600
SCREENHEIGHT = 480

screen = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))

pygame.init();

running = True

time = 0
timeStep = 0.001
timeEnd = 20

J = 1
pRadius = 20
theta = 0
thetaDot = 0

y = 200
yDot = 0
m = 100
k = 10**3
b = 10
g = 9.81
h = 2
counter = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    if y < 0:
        Fd = abs(y)*k + (-yDot*b)
    else:
        Fd = 0

    thetaDotDot = (-m*g+Fd)*pRadius/J



    timePlot[counter] = time
    thetaDotDot[counter] = thetaDotDot

    '''if time >= timeEnd:
        timeStep = 0'''
    mouse = pygame.mouse.get_pressed()
    thetaDot += thetaDotDot*timeStep
    if mouse[0] == True:
        thetaDot = thetaDot + 5
    theta += thetaDot*timeStep
    yDot = thetaDot*pRadius
    y = y + yDot*timeStep
    time = time + timeStep



    screen.fill((255,255,255))
    pulley = pygame.draw.circle(screen, (0,0, 0), (100, 100), pRadius, 2)
    pygame.draw.line(screen, (128,128,128),(pulley[0]+pulley[2]/2, pulley[1]+pulley[3]/2), (pulley[0]+pulley[2]/2+pRadius*math.cos(theta), pulley[1]+pulley[3]/2+pRadius*math.sin(theta)))
    mass1 = pygame.draw.rect(screen, (0,0,128), (64, -y+SCREENHEIGHT-100, 16,16))
    print(theta)


    pygame.display.update()