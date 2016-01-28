import pygame, sys
from pygame.locals import *
from PlayerC import *
from soldierclass import *
from Draw import *
from nodeclass import *

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
train1 = pygame.image.load('Gamebord 2.png')
sol1 = pygame.image.load('soll.png')

def Draw(sl):
    while sl.IsEmpty == False:
        tempS = sl.Value
        DISPLAYSURF.blit(tempS.Texture,(tempS.PositionX,tempS.PositionY))
        sl = sl.Tail

def Main(menu,player1,player1soldaat):
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


    while l.IsEmpty == False:
        tempL = l.Value
        if event.type == MOUSEBUTTONUP and mousex > l.PositionX and mousex < (l.PositionX + 42) and mousey > l.PositionY and mousey < (l.PositionY + 42)
                l.PositionX = l.PositionX + 42

        l.Value = l.Tail

def VergelijkXN(l)
    while l.IsEmpty == False:
        tempL = l.Value
        if event.type == MOUSEBUTTONUP and mousex > l.PositionX and mousex < (l.PositionX + 42) and mousey > l.PositionY and mousey < (l.PositionY + 42)
                l.PositionX = l.PositionX - 42

        l.Value = l.Tail


def VergelijkYP(l)
    while l.IsEmpty == False:
        tempL = l.Value
        if event.type == MOUSEBUTTONUP and mousex > l.PositionX and mousex < (l.PositionX + 42) and mousey > l.PositionY and mousey < (l.PositionY + 42)
                l.PositionY = l.PositionY + 42

        l.Value = l.Tail

def VergelijkYN(l)
    while l.IsEmpty == False:
        tempL = l.Value
        if event.type == MOUSEBUTTONUP and mousex > l.PositionX and mousex < (l.PositionX + 42) and mousey > l.PositionY and mousey < (l.PositionY + 42)
                l.PositionY = l.PositionY - 42

        l.Value = l.Tail


    while start == True:
        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(spelImg, (0 ,0))
        Draw(player1soldaat)
        for event in pygame.event.get():
            if event.type == MOUSEMOTION:
                mousex, mousey = pygame.mouse.get_pos()
            if event.type == KEYUP and event.key == K_ESCAPE or (mousex > 1198 and mousex < 1360 and mousey > 690 and mousey < 763):
                start = False
            if event.type == MOUSEBUTTONUP and mousex > 775 and mousex < 937 and mousey > 440 and mousey < 478:
                start = False
                train = True
            if event.type == MOUSEBUTTONUP and mousex > 775 and mousex < 937 and mousey > 230 and mousey < 268:
                    walk = True
                    fight = False
                    build = False
                    train = False
                    instruction = False
            if event.type == MOUSEBUTTONUP and mousex > 775  and mousex < 937 and mousey > 300 and mousey < 338:
                    walk = False
                    fight = True
                    build = False
                    train = False
                    instruction = False
            if event.type == MOUSEBUTTONUP and mousex > 775 and mousex < 937 and mousey > 370 and mousey < 408:
                    walk = False
                    fight = False
                    build = True
                    train = False
                    instruction = False
            if event.type == MOUSEBUTTONUP and mousex > 775 and mousex < 937 and mousey > 440 and mousey < 478:
                walk = False
            if event.type == MOUSEBUTTONUP and mousex > 802 and mousex < 965 and mousey > 691 and mousey < 730:
                    walk = False
                    fight = False
                    build = False
                    train = False
                    instruction = True
            if event.type == MOUSEBUTTONUP and mousex > 998 and mousex < 1160 and mousey > 725 and mousey < 763:
                end = True







            pygame.display.update()


    while train == True:
        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(train1, (0 ,0))
        Draw(player1soldaat)
        for event in pygame.event.get():
            if event.type == MOUSEMOTION:
                mousex, mousey = pygame.mouse.get_pos()
            if event.type == KEYUP and event.key == K_ESCAPE or (mousex > 1198 and mousex < 1360 and mousey > 690 and mousey < 763):
                train = False
            if event.type == MOUSEBUTTONUP and mousex > 936 and mousex < 1114 and mousey > 259 and mousey < 296:
                soldaat = True
                train = False
            pygame.display.update()

    while soldaat == True:
        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(train1, (0 ,0))
        Draw(player1soldaat)
        for event in pygame.event.get():
            if event.type == MOUSEMOTION:
                mousex, mousey = pygame.mouse.get_pos()
            if event.type == MOUSEBUTTONUP and mousex > player1.startPosX and mousex < (player1.startPosX + 42) and mousey > player1.startPosY and mousey < (player1.startPosY +42):
                player1soldaat = Node(Soldier(sol1,(player1.startPosX+42),player1.startPosY),player1soldaat)
            pygame.display.update()

    
    while walk == True:
        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(trainn1, (0m 0))
        Draw(player1soldaat)
        for event in pygame.event.get():
            if event.type == MOUSEMOTION:
                mousex, mousey = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP and mousex > player1soldaat.PositionX and mousex < (player1soldaat.PositionX) and mousey > player1soldaat.PositionY and mousey < (player1soldaat.PositionY):
                                player1soldaat = Node(Soldier(sol1,(player1soldaat.PositionX),player1soldaat.Positiony),player1soldaat)
                                            pygame.display.update()
                


    Main(False,player1,player1soldaat)
player1 = Player(1,1,500,240,750,150,500,1000)
player1soldaat = Empty


Main(True,player1,player1soldaat)

 while rules == True:
##        DISPLAYSURF.fill(WHITE)
##        DISPLAYSURF.blit(rules1, (500,0))
##        DISPLAYSURF.blit(nextbutton, (1400,800))
##
##        for event in pygame.event.get():
##            if event.type == MOUSEMOTION:
##                mousex, mousey = pygame.mouse.get_pos()
##            if event.type == KEYUP and event.key == K_ESCAPE:
##                rules = False
##            if event.type == MOUSEBUTTONUP and mousex > 1400 and mousex < 1591 and mousey > 800 and mousey < 844: #rules
##                menu = False
##                start = False
##                rules = False
##                rulespage2 = True
##            pygame.display.update()
##
##    while rulespage2 == True:
##        DISPLAYSURF.fill (WHITE)
##        DISPLAYSURF.blit (rules2, (0,0))
##        DISPLAYSURF.blit (nextbutton,(1400,800))
##        DISPLAYSURF.blit (backbutton,(1,800))
##
##        for event in pygame.event.get():
##            if event.type == MOUSEMOTION:
##                mousex, mousey = pygame.mouse.get_pos()
##            if event.type == KEYUP and event.key == K_ESCAPE:
##                rulespage2 = False
##            if event.type == MOUSEBUTTONUP and mousex > 1400 and mousex < 1591 and mousey > 800 and mousey < 944:
##                rulespage2 = False
##                rulespage3 = True
##            pygame.display.update()
##
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
##                pygame.display.update ()
