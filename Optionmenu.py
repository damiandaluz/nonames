           if event.type == MOUSEBUTTONUP and mousex > 925 and mousex < 988 and mousey > 360 and mousey < 404: #low
                pygame.mixer.music.set_volume(0.1)

            if event.type == MOUSEBUTTONUP and mousex > 1000 and mousex < 1125 and mousey > 360 and mousey < 404: #medium
                pygame.mixer.music.set_volume(0.5)

            if event.type == MOUSEBUTTONUP and mousex > 1135 and mousex < 1205 and mousey > 360 and mousey < 404: #hard
                pygame.mixer.music.set_volume(1)

            if event.type == MOUSEBUTTONUP and mousex > 1215 and mousex < 1300 and mousey > 360 and mousey < 404: #mute
                pygame.mixer.music.set_volume(0)



