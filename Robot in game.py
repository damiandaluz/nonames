def Draw(sl):
    while sl.IsEmpty == False:
        tempS = sl.Value
        DISPLAYSURF.blit(tempS.Texture,(tempS.PositionX,tempS.PositionY))
        sl = sl.Tail


def Main(menu,player1,player1soldaat,player1tank):
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
        Draw(player1soldaat)
        Draw(player1tank)
        Draw(player1robot)
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

















while Tank == True:
        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(train1, (0 ,0))
        Draw(player1tank)
        Draw(player1soldaat)
        Draw(player1robot)
        for event in pygame.event.get():
            if event.type == MOUSEMOTION:
                mousex, mousey = pygame.mouse.get_pos()
            if event.type == MOUSEBUTTONUP and mousex > player1.startPosX and mousex < (player1.startPosX + 42) and mousey > player1.startPosY and mousey < (player1.startPosY +42):
                player1tank = Node(Tank(tank1,(player1.startPosX+42),player1.startPosY),player1tank)
            pygame.display.update()

while train == True:
        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(train1, (0 ,0))
        Draw(player1soldaat)
        Draw(player1tank)
        Draw(player1robot)
        for event in pygame.event.get():
            if event.type == MOUSEMOTION:
                mousex, mousey = pygame.mouse.get_pos()
            if event.type == KEYUP and event.key == K_ESCAPE or (mousex > 1198 and mousex < 1360 and mousey > 690 and mousey < 763):
                train = False
            if event.type == MOUSEBUTTONUP and mousex > 936 and mousex < 1114 and mousey > 259 and mousey < 296:
                soldaat = True
                train = False
            if event.type == MOUSEBUTTONUP and mousex > 931 and mousex < 1110 and mousey > 417 and mousey < 455:
                soldaat = False
                train = False
                tank = True
                robot = False
            if event.type == MOUSEBUTTONUP and mousex > 936 and mousex < 1114 and mousey > 332 and mousey < 372:
                robot = True

            pygame.display.update()


while robot == True:
        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(train1, (0 ,0))
        Draw(player1tank)
        Draw(player1soldaat)
        Draw(player1robot)
        for event in pygame.event.get():
            if event.type == MOUSEMOTION:
                mousex, mousey = pygame.mouse.get_pos()
            if event.type == MOUSEBUTTONUP and mousex > player1.startPosX and mousex < (player1.startPosX + 42) and mousey > player1.startPosY and mousey < (player1.startPosY +42):
                player1robot = Node(Robot(robot1,(player1.startPosX+42),player1.startPosY),player1robot)
            pygame.display.update()




Main(False,player1,player1soldaat,player1tank)
player1 = Player(1,1,500,240,750,150,500,1000)
player1soldaat = Empty
player1tank = Empty
player1robot = Empty


Main(True,player1,player1soldaat,player1tank, player1robot)
