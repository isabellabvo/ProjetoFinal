def gameover_screen(screen):
    click = False
    while True:
        screen.blit(fundoinicial,(0,0))
        draw_text('GAME OVER', font, (255, 0, 0), screen, 140, 10)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(150, 200, 200, 50)
        button_2 = pygame.Rect(150, 350, 200, 50)

        if button_1.collidepoint((mx, my)):
            if click:
                return TELA_MENU

        if button_2.collidepoint((mx, my)):
            if click:
                return SAIR

        pygame.draw.rect(screen, (0, 0, 0), button_1)
        pygame.draw.rect(screen, (0, 0, 0), button_2)
        draw_text('Reiniciar', font3, (255, 215, 0), screen, 195, 215)
        draw_text('Sair', font3, (255, 215, 0), screen, 220, 365)
        draw_text("Que pena! Tente novamente", font3,  (0, 0, 0), screen, 90, 150)
 
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                return SAIR
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return SAIR
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
