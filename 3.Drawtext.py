def draw_text(text, font, color, surface, x, y):
    '''função responsável por desenhar os textos na tela
        argumentos - text: texto, font: fonte do texto, color: cor do texto, surface: superfície da tela, x y: posição nos eixos x e y respectivamente'''
    textobj = font.render(text, 1, color) #renderiza o texto
    textrect = textobj.get_rect() #consegue a área retangular da superfície
    textrect.topleft = (x, y) #define as coordenadas
    surface.blit(textobj, textrect) #coloca o texto na tela
click = False #Cria uma variável para o clique
