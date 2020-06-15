def options(screen):
    '''função responsável para criar a tela de opções, ou seja, a área onde a jogador pode escolher o bloco com o qual ele irá jogar
        argumentos - screen: projeção da tela
        o que retorna - responsável por retornar a tela opção com os botões referentes aos blocos '''

    click = False
    running = True
    while running:

        mx, my = pygame.mouse.get_pos()
        screen.fill((255,200,0))
        button1 = pygame.Rect(135, 100, 200, 130)
        button2 = pygame.Rect(135, 250, 200, 130)
        button3 = pygame.Rect(135, 400, 200, 130)

        pygame.draw.rect(screen, (0, 0, 0), button1)
        pygame.draw.rect(screen, (0, 0, 0), button2)
        pygame.draw.rect(screen, (0, 0, 0), button3)
        
        blocomario = pygame.image.load("bloco mario.png").convert() #Carrega e converte a imagem do bloco da opção Mario 
        blocomario = pygame.transform.scale(blocomario, (100, 100)) #Coloca em escala e define a posição
        screen.blit(blocomario,(185,110)) #Coloca na tela 
        
        blocominecraft = pygame.image.load("bloco minecraft.jpg").convert() #Carrega e converte a imagem do bloco da opção Minecraft 
        blocominecraft = pygame.transform.scale(blocominecraft, (100, 100))  #Coloca em escala e define a posição
        screen.blit(blocominecraft,(185, 265)) #Coloca na tela 
        
        
        bloconormal = pygame.image.load("block.png").convert() #Carrega e converte a imagem do bloco da opção Padrão 
        bloconormal = pygame.transform.scale(bloconormal, (130, 80))  #Coloca em escala e define a posição
        screen.blit(bloconormal,(170, 422)) #Coloca na tela 



        if button1.collidepoint((mx, my)): #Condição caso o botão 1 seja clicado
            if click:
                return TELA_JOGO_MARIO #Retorna a tela personalizada do Mario
        if button2.collidepoint((mx, my)): #Condição caso o botão 2 seja clicado
            if click:
                return TELA_JOGO_MINECRAFT #Retorna a tela personalizada do Minecraft
        if button3.collidepoint((mx,my)): #Condição caso o botão 3 seja clicado
            if click:
                return TELA_JOGO_NORMAL #Retorna a tela personalizada ao Padrão

        draw_text('Escolha o seu bloco!', font, (255, 0, 0), screen, 17, 20) #Desenha na tela o texto "Escolha o seu bloco!
        
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
