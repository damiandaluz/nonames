if event.type == MOUSEMOTION:
                    mousex, mousey = pygame.mouse.get_pos()
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE) or (event.type == MOUSEBUTTONUP and mousex > 928.5 and mousex < 778.5 and mousey > 475 and mousey < 519):
                    pygame.quit()
                    sys.exit()

            if event.type == MOUSEBUTTONUP and mousex > 775 and mousex < 937 and mousey > 230 and mousey < 268:
                    walk = True
                    fight = False
                    build = False
                    train = False
                    instruction = False





            if event.type == MOUSEBUTTONUP and mousex > 775  and mousex < 937 and mousey > 300 and mousey < 338: #player 2
                    walk = False
                    fight = True
                    build = False
                    train = False
                    instruction = False


            if event.type == MOUSEBUTTONUP and mousex > 775 and mousex < 937 and mousey > 370 and mousey < 408: #player 4
                    walk = False
                    fight = False
                    build = True
                    train = False
                    instruction = False



            if event.type == MOUSEBUTTONUP and mousex > 775 and mousex < 937 and mousey > 440 and mousey < 478: #rules
                    walk = False
                    fight = False
                    build = False
                    train = True
                    instruction = False


            if event.type == MOUSEBUTTONUP and mousex > 802 and mousex < 965 and mousey > 691 and mousey < 730: #rules
                    walk = False
                    fight = False
                    build = False
                    train = False
                    instruction = True







            pygame.display.update()
