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
