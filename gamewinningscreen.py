import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((1366,768))
pygame.display.set_caption('Frequency')
WHITE = (255, 255, 255)
RED = (255,   0,   0)
SpelImg = pygame.image.load('menu.png')
#pygame.draw.rect(DISPLAYSURF, RED, (200, 150, 100, 50))
start2Img = pygame.image.load('two players.png')
start4Img = pygame.image.load('four players.png')
rulesImg = pygame.image.load ('rules.png')
spelImg = pygame.image.load('Gamebord.png')
endImg = pygame.image.load('end.png')
rules1 = pygame.image.load('1.png')
rules2 = pygame.image.load('2.png')
nextbutton = pygame.image.load('next.png')
backbutton = pygame.image.load('back.png')
rulesquick = pygame.image.load ('quickrules.png')
winningscreen = pygame.image.load('winning screen.png')

def Main():
    menu = True
    while menu == True:
        start = False
        rules = False
        rulespage2 = False
        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(SpelImg, (0,0))
        DISPLAYSURF.blit(start2Img, (928.5,250))
        DISPLAYSURF.blit(start4Img, (928.5,325))
        DISPLAYSURF.blit(rulesImg, (928.5,400))
        DISPLAYSURF.blit(endImg,(928.5,475))
        for event in pygame.event.get():

            if event.type == MOUSEMOTION:
                    mousex, mousey = pygame.mouse.get_pos()
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE) or (event.type == MOUSEBUTTONUP and mousex > 928.5 and mousex < 778.5 and mousey > 475 and mousey < 519):
                    pygame.quit()
                    sys.exit()

            if event.type == MOUSEBUTTONUP and mousex > 928.5 and mousex < 1042.5 and mousey > 200 and mousey < 244:
                    DISPLAYSURF.blit(spelImg, (0,0))

            if event.type == MOUSEBUTTONUP and mousex > 928.5 and mousex < 1042.5 and mousey > 250 and mousey < 294: #player 2
                    menu = False
                    start = True
                    rules = False
                    rulespage2 = False

            if event.type == MOUSEBUTTONUP and mousex > 928.5 and mousex < 1042.5 and mousey > 325 and mousey < 369: #player 4
                    menu = False
                    start = True
                    rules = False
                    rulespage2 = False


            if event.type == MOUSEBUTTONUP and mousex > 928.5 and mousex < 1042.5 and mousey > 400 and mousey < 444: #rules
                    menu = False
                    start = False
                    rules = True
                    rulespage2 = False



            pygame.display.update()

    while start == True:
        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(spelImg, (0 ,0))
        for event in pygame.event.get():
            if event.type == MOUSEMOTION:
                mousex, mousey = pygame.mouse.get_pos()
            if event.type == KEYUP and event.key == K_ESCAPE:
                start = False
            pygame.display.update()

    while rules == True:
        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(winningscreen, (0,0))
        DISPLAYSURF.blit(nextbutton, (1400,800))

        for event in pygame.event.get():
            if event.type == MOUSEMOTION:
                mousex, mousey = pygame.mouse.get_pos()
            if event.type == KEYUP and event.key == K_ESCAPE:
                rules = False
            if event.type == MOUSEBUTTONUP and mousex > 1400 and mousex < 1591 and mousey > 800 and mousey < 844: #rules
                menu = False
                start = False
                rules = False
                rulespage2 = True
            pygame.display.update()

    while rulespage2 == True:
        DISPLAYSURF.fill (WHITE)
        DISPLAYSURF.blit (winningscreen, (0,0))
        DISPLAYSURF.blit (nextbutton,(1400,800))
        DISPLAYSURF.blit (backbutton,(1,800))

        for event in pygame.event.get():
            if event.type == MOUSEMOTION:
                mousex, mousey = pygame.mouse.get_pos()
            if event.type == KEYUP and event.key == K_ESCAPE:
                rulespage2 = False
            if event.type == MOUSEBUTTONUP and mousex > 1400 and mousex < 1591 and mousey > 800 and mousey < 944:
                rulespage2 = False
                rulespage3 = True
            pygame.display.update()




    wh

##    while rulespage3 == True:
##        DISPLAYSURF.fill (WHITE)
##        DISPLAYSURF.blit (rulesquick, (0,0))
##        DISPLAYSURF.blit (nextbutton,(1400,800))
##        DISPLAYSURF.blit (backbutton,(1,800))
##
##        for event in pygame.event.get():
##            if event.type == MOUSEMOTION:
##                mousex, mousey = pygame.mouse.get_pos()
##
##            if event.type == KEYUP and event.key == K_ESCAPE:
##                rulespage3 = False
##
##
##        pygame.display.update ()



    Main()

Main()
