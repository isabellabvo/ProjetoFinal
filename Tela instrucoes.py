def instrucoes(screen):
    click = False
    while True:
        screen.blit(fundoinicial,(0,0))
        draw_text('Instruções', font, (255, 0, 0), screen, 150, 10)

        mx, my = pygame.mouse.get_pos()
 
        button_1 = pygame.Rect(25, 500, 200, 50)
        button_2 = pygame.Rect(250, 500, 200, 50)

        if button_1.collidepoint((mx, my)):
            if click:
                return TELA_MENU

        if button_2.collidepoint((mx, my)):
            if click:
                return TELA_OPTIONS

        pygame.draw.rect(screen, (0, 0, 0), button_1)
        pygame.draw.rect(screen, (0, 0, 0), button_2)

        draw_text('Bem vindo ao jogo Tower Blocks!', font3, (0, 0, 0), screen, 50, 100)
        draw_text("A principal missão é construir a maior torre possível!", font2,  (0, 0, 0), screen, 30, 150)
        draw_text("Para soltar o bloco é só apertar a tecla ESPAÇO!", font2,  (0, 0, 0), screen, 30, 200)
        draw_text("Mas cuidado para não deixar o bloco cair no chão...", font2,  (0, 0, 0), screen, 30, 250)
        draw_text("A medida que você constrói sua torre...", font2,  (0, 0, 0), screen, 75, 300)
        draw_text("o nível vai aumentando e o tempo acabando!", font2,  (0, 0, 0), screen, 55, 350)
        draw_text("Vai encarar esse desafio?", font3, (0, 0, 0), screen, 90, 400)
        draw_text('Voltar ao menu principal', font2, (255, 215, 0), screen, 24, 518)
        draw_text('Jogar', font2, (255, 215, 0), screen, 325, 518)

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
