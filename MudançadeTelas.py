tela_atual = TELA_MENU
while tela_atual != SAIR:
    if tela_atual == TELA_MENU:
        tela_atual = main_menu(screen)
    elif tela_atual == TELA_OPTIONS:
        tela_atual = options(screen)
    elif tela_atual == TELA_INSTRUCOES:
        tela_atual = instrucoes(screen)
    elif tela_atual in [TELA_JOGO_MARIO, TELA_JOGO_NORMAL, TELA_JOGO_MINECRAFT]:
        tela_atual = game_screen(screen, tela_atual)
    elif tela_atual == TELA_GAMEOVER:
        tela_atual = gameover_screen(screen)
