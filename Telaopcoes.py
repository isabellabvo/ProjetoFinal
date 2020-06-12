def options(screen):
    click = False
    running = True
    while running:

        mx, my = pygame.mouse.get_pos()
        screen.fill((255,200,0))
        button1 = pygame.Rect(135, 100, 200, 130)
        button2 = pygame.Rect(135, 250, 200, 130)
        button3 = pygame.Rect(135, 400, 200, 130)

        pygame.draw.rect(screen, (255, 0, 0), button1)
        pygame.draw.rect(screen, (255, 0, 0), button2)
        pygame.draw.rect(screen, (255, 0, 0), button3)
        
        blocomario = pygame.image.load("bloco mario.png").convert()
        screen.blit(blocomario,(100,100))

        if button1.collidepoint((mx, my)):
            if click:
                #gametower()
                return TELA_JOGO
        if button2.collidepoint((mx, my)):
            if click:
                #gamemario()
                return TELA_JOGO
        if button3.collidepoint((mx,my)):
            if click:
                #gameminecraft()
                return TELA_JOGO

        draw_text('Escolha o seu bloco!', font, (255, 255, 255), screen, 65, 20)
        
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
        mainClock.tick(10)
