import pygame, sys
from pygame.locals import *
from PlayerC import *
from soldierclass import *
from nodeclass import *
from tankclass import *
from barakclass import *
from basisclass import *
from robotclass import *

pygame.mixer.init()
pygame.mixer.music.load("bgm.mp3")
pygame.mixer.music.play()
    


pygame.init()
DISPLAYSURF = pygame.display.set_mode((1366,768), FULLSCREEN)
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
sol1 = pygame.image.load('sol1.png')
sol2 = pygame.image.load('sol2.png')
sol3 = pygame.image.load('sol3.png')
sol4 = pygame.image.load('sol4.png')
rob1 = pygame.image.load('rob1.png')
rob2 = pygame.image.load('rob2.png')
rob3 = pygame.image.load('rob3.png')
rob4 = pygame.image.load('rob4.png')
tank1 = pygame.image.load('tank1.png')
tank2 = pygame.image.load('tank2.png')
tank3 = pygame.image.load('tank3.png')
tank4 = pygame.image.load('tank4.png')
barak1 = pygame.image.load('barak1.png')
barak2 = pygame.image.load('barak2.png')
barak3 = pygame.image.load('barak3.png')
barak4 = pygame.image.load('barak4.png')
playerbasis1 = pygame.image.load('playerbasis1.png')
walk1 = pygame.image.load('Gamebord 3.png')
walk = pygame.image.load('Gamebord 4.png')
walks = pygame.image.load('GamebordWS.png')
trains = pygame.image.load('GamebordTS.png')

def Draw(sl):
    if sl.IsEmpty == True:
        return
    else:
        tempS = sl.Value
        DISPLAYSURF.blit(tempS.Texture,(tempS.PositionX,tempS.PositionY))
        sl = sl.Tail

def CheckUp(l,x,y):
    while l.IsEmpty == False:
        tempL = l.Value
        if x > tempL.PositionX and x < (tempL.PositionX + 42) and y > tempL.PositionY and y < (tempL.PositionY + 42):
            tempL.PositionY = tempL.PositionY - 42
            l.Value.PositionX = tempL.PositionX
            Main(False,True,False,False,False,False,False,False,False,False,False,False,player1robot,player1tank,player1,player1soldaat)
        else: l.Value = l.Tail

def CheckDown(l,x,y):
    while l.IsEmpty == False:
        tempL = l.Value
        if x > tempL.PositionX and x < (tempL.PositionX + 42) and y > tempL.PositionY and y < (tempL.PositionY + 42):
            tempL.PositionY = tempL.PositionY + 42
            l.Value.PositionX = tempL.PositionX
            Main(False,True,False,False,False,False,False,False,False,False,False,False,player1robot,player1tank,player1,player1soldaat)
        else: l.Value = l.Tail

def CheckLeft(l,x,y):
    while l.IsEmpty == False:
        tempL = l.Value
        if x > tempL.PositionX and x < (tempL.PositionX + 42) and y > tempL.PositionY and y < (tempL.PositionY + 42):
            tempL.PositionX = tempL.PositionX - 42
            l.Value.PositionX = tempL.PositionX
            Main(False,True,False,False,False,False,False,False,False,False,False,False,player1robot,player1tank,player1,player1soldaat)
        else: l.Value = l.Tail

def CheckRight(l,x,y):
    while l.IsEmpty == False:
        tempL = l.Value
        if x > tempL.PositionX and x < (tempL.PositionX + 42) and y > tempL.PositionY and y < (tempL.PositionY + 42):
            tempL.PositionX = tempL.PositionX + 42
            l.Value.PositionX = tempL.PositionX
            Main(False,True,False,False,False,False,False,False,False,False,False,False,player1robot,player1tank,player1,player1soldaat)
        else: l.Value = l.Tail



def Main(menu,start,walkw,soldaatw,soldaatwr,soldaatwd,soldaatwu,soldaatwl,soldaattr,robottr,tanktr,walks1,plr,player1tank,player1,pls):
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
        Draw(player1tank)
        Draw(pls)
        Draw(plr)
        Draw(player1basis)
        for event in pygame.event.get():
            if event.type == MOUSEMOTION:
                mousex, mousey = pygame.mouse.get_pos()
            if event.type == KEYUP and event.key == K_ESCAPE or (event.type == MOUSEBUTTONUP and mousex > 1198 and mousex < 1360 and mousey > 690 and mousey < 763):
                start = False
            if event.type == MOUSEBUTTONUP and mousex > 775 and mousex < 937 and mousey > 440 and mousey < 478:
                start = False
                train = True
            if event.type == MOUSEBUTTONUP and mousex > 775 and mousex < 937 and mousey > 230 and mousey < 268:
                walkw = True
                start = False
            if event.type == MOUSEBUTTONUP and mousex > 775  and mousex < 937 and mousey > 300 and mousey < 338:
                fight = True
                start = False
            if event.type == MOUSEBUTTONUP and mousex > 775 and mousex < 937 and mousey > 370 and mousey < 408:
                start = False
                build = True
            if event.type == MOUSEBUTTONUP and mousex > 775 and mousex < 937 and mousey > 440 and mousey < 478:
                walkw = False
            if event.type == MOUSEBUTTONUP and mousex > 802 and mousex < 965 and mousey > 691 and mousey < 730:
                start = False
                instruction = True
            if event.type == MOUSEBUTTONUP and mousex > 998 and mousex < 1160 and mousey > 725 and mousey < 763:
                    endturn = True
            pygame.display.update()

    while walkw == True:
        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(walk,(0,0))
        Draw(player1tank)
        Draw(pls)
        Draw(plr)
        Draw(player1basis)
        for event in pygame.event.get():
            if event.type == MOUSEMOTION:
                mousex,mousey = pygame.mouse.get_pos()
            if event.type == KEYUP and event.key == K_ESCAPE:
                walkw = False
            if event.type == MOUSEBUTTONUP and mousex > 938 and mousex < 1114 and mousey > 258 and mousey < 297:
                soldaatw = True
                walkw = False
            pygame.display.update()


    while soldaatw == True:
        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(walk1,(0,0))
        Draw(player1tank)
        Draw(pls)
        Draw(plr)
        Draw(player1basis)
        for event in pygame.event.get():
            if event.type == MOUSEMOTION:
                mousex,mousey = pygame.mouse.get_pos()
            if event.type == KEYUP and event.key == K_ESCAPE:
                soldaatw = False
            if event.type == MOUSEBUTTONUP and mousex > 1137 and mousex < 1314 and mousey > 302 and mousey < 341:
                soldaatw = False
                soldaatwr = True
            if event.type == MOUSEBUTTONUP and mousex > 959 and mousex < 1137 and mousey > 262 and mousey < 301:
                soldaatw = False
                soldaatwu = True
            if event.type == MOUSEBUTTONUP and mousex > 959 and mousex < 1138 and mousey > 342 and mousey < 381:
                soldaatw = False
                soldaatwd = True
            if event.type == MOUSEBUTTONUP and mousex > 781 and mousex < 960 and mousey > 302 and mousey < 341:
                soldaatw = False
                soldaatwl = True
            pygame.display.update()

    while soldaatwr == True:
        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(walks,(0,0))
        Draw(player1tank)
        Draw(pls)
        Draw(plr)
        Draw(player1basis)
        global player1soldaat
        for event in pygame.event.get():
            if event.type == MOUSEMOTION:
                mousex,mousey = pygame.mouse.get_pos()
            if event.type == KEYUP and event.key == K_ESCAPE:
                soldaatwr = False
            if event.type == MOUSEBUTTONUP:
                CheckRight(player1soldaat,mousex,mousey)
            pygame.display.update()

    while soldaatwu == True:
        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(walks,(0,0))
        Draw(player1tank)
        Draw(pls)
        Draw(plr)
        Draw(player1basis)
        global player1soldaat
        for event in pygame.event.get():
            if event.type == MOUSEMOTION:
                mousex,mousey = pygame.mouse.get_pos()
            if event.type == KEYUP and event.key == K_ESCAPE:
                soldaatwu = False
            if event.type == MOUSEBUTTONUP:
                CheckUp(player1soldaat,mousex,mousey)
            pygame.display.update()

    while soldaatwd == True:
        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(walks,(0,0))
        Draw(player1tank)
        Draw(pls)
        Draw(plr)
        Draw(player1basis)
        global player1soldaat
        for event in pygame.event.get():
            if event.type == MOUSEMOTION:
                mousex,mousey = pygame.mouse.get_pos()
            if event.type == KEYUP and event.key == K_ESCAPE:
                soldaatwd = False
            if event.type == MOUSEBUTTONUP:
                CheckDown(player1soldaat,mousex,mousey)
            pygame.display.update()

    while soldaatwl == True:
        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(walks,(0,0))
        Draw(player1tank)
        Draw(pls)
        Draw(plr)
        Draw(player1basis)
        global player1soldaat
        for event in pygame.event.get():
            if event.type == MOUSEMOTION:
                mousex,mousey = pygame.mouse.get_pos()
            if event.type == KEYUP and event.key == K_ESCAPE:
                soldaatwl = False
            if event.type == MOUSEBUTTONUP:
                CheckLeft(player1soldaat,mousex,mousey)
            pygame.display.update()


    while train == True:
        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(train1, (0 ,0))
        Draw(player1tank)
        Draw(pls)
        Draw(plr)
        Draw(player1basis)
        for event in pygame.event.get():
            if event.type == MOUSEMOTION:
                mousex, mousey = pygame.mouse.get_pos()
            if event.type == KEYUP and event.key == K_ESCAPE or (mousex > 1198 and mousex < 1360 and mousey > 690 and mousey < 763):
                train = False
            if event.type == MOUSEBUTTONUP and mousex > 936 and mousex < 1114 and mousey > 259 and mousey < 296:
                soldaattr = True
                train = False
            if event.type == MOUSEBUTTONUP and mousex > 931 and mousex < 1110 and mousey > 417 and mousey < 455:
                train = False
                tanktr = True
            if event.type == MOUSEBUTTONUP and mousex > 936 and mousex < 1114 and mousey > 332 and mousey < 372:
                robottr = True
                train = False
            pygame.display.update()

    while robottr == True:
            DISPLAYSURF.fill(WHITE)
            DISPLAYSURF.blit(trains, (0 ,0))
            Draw(player1tank)
            Draw(pls)
            Draw(plr)
            Draw(player1basis)
            for event in pygame.event.get():
                if event.type == MOUSEMOTION:
                    mousex, mousey = pygame.mouse.get_pos()
                if event.type == MOUSEBUTTONUP and mousex > player1.startPosX and mousex < (player1.startPosX + 42) and mousey > player1.startPosY and mousey < (player1.startPosY +42):
                    player1robot = Node(Robot(rob1,(player1.startPosX+42),player1.startPosY),player1robot)
                    player1.Money = player1.Money - 300
                    Main(False,True,False,False,False,False,False,False,False,False,False,False,player1robot,player1tank,player1,player1soldaat)
            pygame.display.update()

    while tanktr == True:
        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(trains, (0 ,0))
        Draw(player1tank)
        Draw(pls)
        Draw(plr)
        Draw(player1basis)
        for event in pygame.event.get():
            if event.type == MOUSEMOTION:
                mousex, mousey = pygame.mouse.get_pos()
            if event.type == MOUSEBUTTONUP and mousex > player1.startPosX and mousex < (player1.startPosX + 42) and mousey > player1.startPosY and mousey < (player1.startPosY +42):
                player1tank = Node(Tank(tank1,(player1.startPosX+42),player1.startPosY),player1tank)
                player1.Money = player1.Money - 750
                Main(False,True,False,False,False,False,False,False,False,False,False,False,player1robot,player1tank,player1,player1soldaat)
            pygame.display.update()

    while soldaattr == True:
        global player1soldaat
        global player1robot
        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(trains, (0 ,0))
        Draw(player1tank)
        Draw(pls)
        Draw(plr)
        Draw(player1basis)
        for event in pygame.event.get():
            if event.type == MOUSEMOTION:
                mousex, mousey = pygame.mouse.get_pos()
            if event.type == MOUSEBUTTONUP and mousex > player1.startPosX and mousex < (player1.startPosX + 42) and mousey > player1.startPosY and mousey < (player1.startPosY +42):
                player1soldaat = Node(Soldier(sol1,(player1.startPosX+42),player1.startPosY),player1soldaat)
                player1.Money = player1.Money - 150
                Main(False,True,False,False,False,False,False,False,False,False,False,False,player1robot,player1tank,player1,player1soldaat)
            pygame.display.update()


##    while walk == True:
##        DISPLAYSURF.fill(WHITE)
##        DISPLAYSURF.blit(train1, (0 ,0))
##        Draw(player1soldaat)
##        for event in pygame.event.get():
##            if event.type == MOUSEMOTION:
##                mousex, mousey = pygame.mouse.get_pos()
##            if event.type == MOUSEBUTTONUP and mousex > 936 and mousex < 1114 and mousey > 259 and mousey < 296:
##                soldaatw = True
##                walk = False
##                Main(False,True,False,False,player1,player1soldaat)
##            pygame.display.update()

##    while rules == True:
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
##        pygame.display.update ()



    Main(True,False,False,False,False,False,False,False,False,False,False,False,player1robot,player1tank,player1,player1soldaat)
player1 = Player(1,1,500,240,750,150,500,1000)
player1tank = Empty
player1robot = Empty
player1soldaat = Empty
player1basis = Node(Basis(playerbasis1,1,1,25),Empty)


Main(True,False,False,False,False,False,False,False,False,False,False,False,player1robot,player1tank,player1,player1soldaat)
