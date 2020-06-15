def main_menu(screen):
    ''' função responsável para criar a tela menu
        argumentos - screen: projeção da tela
        o que retorna - responsável por retornar a tela menu com os botões '''

    click = False
    while True:#Condição caso o botão 2 seja clicado
        screen.blit(fundoinicial,(0,0))#Coloca o fundo inicial na tela
        draw_text('Menu principal', font, (255, 255, 255), screen, 80, 10)#Desenha na tela o texto Menu Principal com a fonte especificada, a cor branca na posição (80,10) 

        mx, my = pygame.mouse.get_pos()#Retorna a posição X e Y do cursor do mouse.
 
        button_1 = pygame.Rect(143, 150, 200, 50)#Cria o botão 1 como um retângulo
        button_2 = pygame.Rect(143, 300, 200, 50)#Cria o botão 2 como um retângulo

        if button_1.collidepoint((mx, my)): #Condição caso o botão 1 seja clicado
            if click:
                return TELA_OPTIONS #Retorna a tela das opções
        if button_2.collidepoint((mx, my)): #Condição caso o botão 2 seja clicado
            if click:
                return TELA_INSTRUCOES #Retorna a tela das instruções

        pygame.draw.rect(screen, (255, 0, 0), button_1) #Desenha o botão 1 (retângulo) na tela
        pygame.draw.rect(screen, (255, 0, 0), button_2) #Desenha o botão 2 (retângulo) na tela
        
        draw_text('Jogar', font, (255, 255, 255), screen, 186, 1445) #Desenha o texto "Jogar" na tela
        draw_text('Instruções', font, (255, 255, 255), screen, 144, 300)) #Desenha o texto "Instruções" na tela
 
        click = False # Definimos o clique como falso
        for event in pygame.event.get():
            if event.type == QUIT: #Condição em que o usuário aperta o QUIT do jogo
                return SAIR #Todas as telas são fechadas
            if event.type == KEYDOWN: #Condição em que o usuário aperta uma tecla 
                if event.key == K_ESCAPE:#Condição em que o usuário aperta a tecla ESC
                    return SAIR #Todas as telas são fechadas
            if event.type == MOUSEBUTTONDOWN: #Condição em que o usuário aperta o mouse
                if event.button == 1: #Condição em que o usuário aperta o lado esquerdo do mouse
                    click = True  #Clique é válido 
 
        pygame.display.update() #Atualiza a tela
