def game_screen(window, modo_jogo):
    if modo_jogo == TELA_JOGO_MARIO:
        background = pygame.image.load('fundo.jpg').convert()
    elif modo_jogo == TELA_JOGO_MINECRAFT:
        background = pygame.image.load('fundo.jpg').convert()
    elif modo_jogo == TELA_JOGO_NORMAL:
        background = pygame.image.load('fundo.jpg').convert()
    background = pygame.transform.scale(background,(WIDTH, HEIGHT))
