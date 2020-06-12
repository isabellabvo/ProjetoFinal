def main_menu(screen):
    click = False
    while True:
        screen.blit(fundoinicial,(0,0))
        draw_text('Menu principal', font, (255, 255, 255), screen, 125, 10)

        mx, my = pygame.mouse.get_pos()
 
        button_1 = pygame.Rect(143, 150, 200, 50)
        button_2 = pygame.Rect(143, 300, 200, 50)

        if button_1.collidepoint((mx, my)):
            if click:
                return TELA_OPTIONS
        if button_2.collidepoint((mx, my)):
            if click:
                return TELA_INSTRUCOES

        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)
        
        draw_text('Jogar', font, (255, 255, 255), screen, 190, 157)
        draw_text('Instruções', font, (255, 255, 255), screen, 155, 310)
 
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
