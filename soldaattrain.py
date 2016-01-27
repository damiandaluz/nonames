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
