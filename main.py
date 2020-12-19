import pygame, sys
from pygame.locals import *
import math
def initPointPos(pointNumberVar, pointNumber, pointX, pointY,segmentLength):
    pointPosPicker = 2
    counter = 0
    for number in pointNumberVar:
        pointNumber.append(counter)
        pointX.append(100)
        pointY.append(pointPosPicker*segmentLength)
        counter += 1
        pointPosPicker += 2

def main():
    clock = pygame.time.Clock()
    pygame.init()
    gravity = 9
    pointsToInit = 1000
    pointNumberVar = []
    pointNumber = []
    pointX = []
    pointY = []
    segmentLength = 1
    mouseXY = pygame.mouse.get_pos()
    velocityX = []
    velocityY = []
    looper = 0
    display = pygame.display.set_mode((700,700),0,32)
    while looper < pointsToInit:
        pointNumberVar.append(0)
        looper += 1
    initPointPos(pointNumberVar, pointNumber, pointX, pointY,segmentLength)
    airResistence = 2
    for number in pointNumberVar:
        velocityX.append(0)
        velocityY.append(0)
    while True:
        mouseXY = pygame.mouse.get_pos()
        clock.tick(60)
        display.fill((255,255,255))
        for index in pointNumber:
            pygame.draw.circle(display, (0, 0, 0), (pointX[index], pointY[index]), 1)
            if index > 0:
                # Forces
                velocityY[index] += gravity - velocityY[index] / airResistence
                pointY[index] += velocityY[index]
                # Forces
                deltaX = pointX[index] - pointX[index - 1]
                deltaY = pointY[index] - pointY[index - 1]
                l = math.sqrt(deltaX ** 2 + deltaY ** 2)
                deltaX = deltaX * (segmentLength/l)
                deltaY = deltaY * (segmentLength/l)
                pointX[index] = pointX[index - 1] + deltaX
                pointY[index] = pointY[index - 1] + deltaY
                velocityX[index] = deltaX
                #velocityX[index] += pointX[index] - oldPointPosX[index] / 2
                #velocityY[index] += pointY[index] - oldPointPosY[index] / 2

            else:
                pointX[index] = mouseXY[0]
                pointY[index] = mouseXY[1]
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

main()