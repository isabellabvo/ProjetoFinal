# ISABELLA OLIVEIRA E LILA HADBA - TOWER BLOCKS
# Inicialização
# Importa e inicia pacotes
import pygame 
from pygame.locals import *
import math
import sys
import pymunk # Biblioteca responsável pela física 2d do jogo
from pymunk import Vec2d # Representa os vetores 2d
import json # Formato JSON é responsável pela troca de informação que pode ser armazenado em um arquivo.

# Mudança do ícone do jogo
programIcon = pygame.image.load('assets/imagens/logo.png')
pygame.display.set_icon(programIcon)

# Definição de diferentes telas como variáveis
SAIR = 0
TELA_MENU = 1
TELA_OPTIONS = 2
TELA_JOGO_MARIO = 3
TELA_JOGO_MINECRAFT = 4
TELA_JOGO_NORMAL = 5
TELA_INSTRUCOES = 6
TELA_GAMEOVER = 7

# Inicialização do pygame
pygame.init()

mainClock = pygame.time.Clock() # Cria uma variável responsável pelo tempo
pygame.display.set_caption('Tower Blocks') # Define o título da janela
screen = pygame.display.set_mode((480, 600)) # Dimensões da janela
font = pygame.font.SysFont("Bauhaus 93", 50) # Cria variável para guardar a fonte "Bauhaus 93" de tamanho 50
font2 = pygame.font.SysFont(None, 25) # Cria variável para guardar a fonte padrão de tamanho 25
font3 = pygame.font.SysFont(None, 35) # Cria variável para guardar a fonte padrão de tamanho 35
font4 = pygame.font.SysFont("Bauhaus 93", 45) # Cria variável para guardar a fonte "Bauhaus 93" de tamanho 45
fundoinicial = pygame.image.load("assets/imagens/construcao.jpg").convert() # Guarda imagem de fundo das telas menu, gameover e instruções

def draw_text(text, font, color, surface, x, y):
    ''' função responsável para desenhar os textos na tela
        argumentos:
        - text: texto
        - font: fonte do texto 
        - color: cor do texto 
        - surface: superfície da tela
        - x y: posição nos eixos x e y da tela respectivamente
    '''
    textobj = font.render(text, 1, color) # Renderiza o texto
    textrect = textobj.get_rect() # Consegue a área retangular da supefície 
    textrect.topleft = (x, y) # Define as coordenadas
    surface.blit(textobj, textrect) # Coloca o texto na tela 

click = False # Cria uma variável para o clique
 
def main_menu(screen):
    ''' função responsável para criar a tela menu
        argumentos:
        - screen: projeção da tela
        o que retorna - responsável por retornar a tela menu com os botões '''
    click = False
    while True:
        screen.blit(fundoinicial,(0,0)) # Coloca o fundo inicial na tela
        draw_text('Menu principal', font, (255, 255, 255), screen, 80, 10) # Desenha na tela o texto Menu Principal com a fonte especificada, a cor branca na posição (80,10) 

        mx, my = pygame.mouse.get_pos() # Retorna a posição X e Y do cursor do mouse.
 
        button_1 = pygame.Rect(143, 150, 200, 50) # Cria o botão 1 como um retângulo
        button_2 = pygame.Rect(143, 300, 200, 50) # Cria o botão 2 como um retângulo

        if button_1.collidepoint((mx, my)): # Condição caso o botão 1 seja clicado
            if click:
                return TELA_OPTIONS # Retorna a tela das opções
        if button_2.collidepoint((mx, my)): # Condição caso o botão 2 seja clicado
            if click:
                return TELA_INSTRUCOES # Retorna a tela das instruções

        pygame.draw.rect(screen, (255, 0, 0), button_1) # Desenha o botão 1 (retângulo) na tela
        pygame.draw.rect(screen, (255, 0, 0), button_2) # Desenha o botão 2 (retângulo) na tela
        
        draw_text('Jogar', font, (255, 255, 255), screen, 186, 145) # Desenha o texto "Jogar" na tela
        draw_text('Instruções', font4, (255, 255, 255), screen, 144, 300) # Desenha o texto "Instruções" na tela
 
        click = False # Definimos o clique como falso
        for event in pygame.event.get(): 
            if event.type == QUIT: # Condição em que o usuário aperta o QUIT do jogo
                return SAIR # Todas as telas são fechadas
            if event.type == KEYDOWN: # Condição em que o usuário aperta uma tecla 
                if event.key == K_ESCAPE: # Condição em que o usuário aperta a tecla ESC
                    return SAIR # Todas as telas são fechadas
            if event.type == MOUSEBUTTONDOWN: # Condição em que o usuário aperta o mouse
                if event.button == 1: # Condição em que o usuário aperta o lado esquerdo do mouse
                    click = True # Clique é válido 
 
        pygame.display.update() # Atualiza a tela

def options(screen):
    '''função responsável para criar a tela de opções, ou seja, a área onde a jogador pode escolher o bloco com o qual ele irá jogar
        argumentos:
        - screen: projeção da tela
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
        
        blocomario = pygame.image.load("assets/imagens/bloco mario.png").convert() # Carrega e converte a imagem do bloco da opção Mario 
        blocomario = pygame.transform.scale(blocomario, (100, 100)) # Coloca em escala e define a posição
        screen.blit(blocomario,(185, 110)) # Coloca na tela 

        blocominecraft = pygame.image.load("assets/imagens/bloco minecraft.jpg").convert() # Carrega e converte a imagem do bloco da opção Minecraft 
        blocominecraft = pygame.transform.scale(blocominecraft, (100, 100))  # Coloca em escala e define a posição
        screen.blit(blocominecraft,(185, 265)) # Coloca na tela 

        bloconormal = pygame.image.load("assets/imagens/block.png").convert() # Carrega e converte a imagem do bloco da opção Padrão 
        bloconormal = pygame.transform.scale(bloconormal, (130, 80))  # Coloca em escala e define a posição
        screen.blit(bloconormal,(170, 422)) # Coloca na tela 


        if button1.collidepoint((mx, my)): # Condição caso o botão 1 seja clicado
            if click:
                return TELA_JOGO_MARIO # Retorna a tela personalizada do Mario
        if button2.collidepoint((mx, my)): # Condição caso o botão 2 seja clicado
            if click:
                return TELA_JOGO_MINECRAFT # Retorna a tela personalizada do Minecraft
        if button3.collidepoint((mx,my)): # Condição caso o botão 3 seja clicado
            if click:
                return TELA_JOGO_NORMAL # Retorna a tela personalizada ao Padrão

        draw_text('Escolha o seu bloco!', font, (255, 0, 0), screen, 17, 20) # Desenha na tela o texto "Escolha o seu bloco!
        
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

def instrucoes(screen):
    ''' função responsável para criar a tela das instruções, ou seja, explicando brevemente como o jogo deve ser jogado
        argumentos:
        - screen: projeção da tela
        o que retorna - responsável por retornar a tela das instruções'''
    click = False
    while True:
        screen.blit(fundoinicial,(0,0))
        draw_text('Instruções', font, (255, 0, 0), screen, 140, 10)

        mx, my = pygame.mouse.get_pos()
 
        button_1 = pygame.Rect(25, 500, 200, 50)
        button_2 = pygame.Rect(250, 500, 200, 50)

        if button_1.collidepoint((mx, my)):  # Condição caso o botão 1 seja clicado
            if click:
                return TELA_MENU # Retorna a tela do menu principal definida na função _menu

        if button_2.collidepoint((mx, my)): # Condição caso o botão 2 seja clicado
            if click:
                return TELA_OPTIONS # Retorna a tela das opções definida na função options

        pygame.draw.rect(screen, (0, 0, 0), button_1)
        pygame.draw.rect(screen, (0, 0, 0), button_2)

        # Desenha de forma fragmentada o texto das instruções na tela
        draw_text('Bem vindo ao jogo Tower Blocks!', font3, (0, 0, 0), screen, 50, 100)
        draw_text("A principal missão é construir a maior torre possível!", font2,  (0, 0, 0), screen, 30, 150)
        draw_text("Para soltar o bloco é só apertar a tecla ESPAÇO!", font2,  (0, 0, 0), screen, 40, 200)
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

 
def carrega_recorde():
    ''' função responsável para guardar o número no arquivo json e se o anterior for menor que o número posterior, atualiza nesse arquivo
        argumentos - 
        o que retorna - responsável por retornar o recorde'''
    with open ("arquivo.json", "rb") as arquivo: # Abre o arquivo.json como um arquivo
        configuracao = json.load(arquivo) # Carrega o arquivo json
        recorde = configuracao["recorde"] # Escreve a string recorde no arquivo
    return recorde # Retorna o valor do maior número atingido (recorde)

def salva_recorde(recorde):
    ''' função responsável para guardar o maior número da função carrega_recorde
        argumentos: 
        - recorde: maior número gerado pelo jogador
        o que retorna - responsável por retornar o print do recorde'''
    cash = {"recorde": recorde} # Adiciona o valor do recorde como um value em um dicionário no arquivo
    with open ("arquivo.json", "w") as arquivo:
        arquivo.write(json.dumps(cash)) # Transforma de volta para JSON
        print(json.dumps(cash)) 

# Gera tela 
WIDTH = 480 # Largura da tela
HEIGHT = 600 # Comprimento da tela 

# Inicia assets
BLOCK_WIDTH = 100 # Largura do Bloco
BLOCK_HEIGHT = 60 # Comprimento do Bloco

block_img = pygame.image.load('assets/imagens/block.png').convert() # Baixa a imagem "block.png" e converte
block_img = pygame.transform.scale(block_img, (BLOCK_WIDTH, BLOCK_HEIGHT)) # Coloca em escala a imagem para ter as dimensões do bloco

COLLTYPE_BLOCK = 1 # Tipo de colisão com o bloco
COLLTYPE_FLOOR = 2 # Tipo de colisão com o chão

# Inicia estruturas de dados
# Definindo os novos tipos
class Block(pygame.sprite.Sprite): # Tipo do pygame
    ''' Classe responsável para definir os parâmetros dos blocos e da física relacionadas a eles
        Métodos - __init__, add_physics_, update
    '''
    def __init__(self, img, camera_y, speedx, is_first):
        '''Método construtor da classe mãe (Sprite).
        
        argumentos:
        -self
        -img: imagem
        -camera_y: movimento no eixo y
        -speedx: velocidade do bloco no eixo x
        -is_first: declaraprimeiro bloco
        '''
        pygame.sprite.Sprite.__init__(self)

        # Acessa os atributos e métodos através do self
        self.orig_img = img
        self.image = img 
        self.rect = self.image.get_rect() # Consegue a área retangular da imagem
        self.rect.centerx = WIDTH // 2 # Define o centro como a divisão inteira por dois da largura
        self.rect.top = 0 # Define o topo do retângulo 
        self.speedx = speedx # Pixels por frame
        self.camera_y = camera_y # Define o movimento do jogo no eixo y
        self.is_first = is_first # Primeiro bloco
        self.physical_block = None  # Vai possibilitar para saber qual é a posição do nosso bloco.

    def add_physics(self, space):
        '''
        Criamos esse método para ser chamado quando queremos adicionar o bloco na simulação física
        Inicialmente ele não faz parte da simulação, pois está andando de um lado para o outro no topo da tela.
        Quando o jogador aperta a tecla ESPAÇO o bloco passa a fazer parte 
        da simulação física e por isso ele cai.
        
        argumentos:
        - space: Espaço do PyMunk
        '''
        # Cria um retângulo com centro na origem (0, 0)
        points = [
            (-BLOCK_WIDTH//2, -BLOCK_HEIGHT//2),
            (-BLOCK_WIDTH//2, BLOCK_HEIGHT//2),
            (BLOCK_WIDTH//2, BLOCK_HEIGHT//2),
            (BLOCK_WIDTH//2, -BLOCK_HEIGHT//2)
        ]
        mass = 10.0  # Define massa do ponto
        moment = pymunk.moment_for_poly(mass, points, (0,0))  # Define o momento da simulação 
        body = pymunk.Body(mass, moment) # Define o corpo com os parâmetros massa e momento
        body.position = (self.rect.centerx, HEIGHT - self.rect.centery + self.camera_y)  # A posição é o centro de massa do corpo (body)
        shape = pymunk.Poly(body, points) # Define o corpo como um polígono
        shape.collision_type = COLLTYPE_BLOCK # Define o tipo de colisão 
        shape.is_first = self.is_first # Define o primeiro bloco
        shape.in_building = False
        shape.friction = 10  # Define o coeficiente de atrito do corpo
        space.add(body, shape)  # Adiciona o novo corpo no espaço
        self.physical_block = body  # Guarda o corpo para usar sua posição na simulação física para atualizar a visualização
        self.physical_shape = shape  # Guarda a forma

    def update(self):
        '''
        Método responsável por atualizar a posição do bloco e a tela
        '''
        # Condição caso o corpo já tenha sido adicionado na simulação física
        if self.physical_block:
            # Para de andar na horizontal. Agora todo o movimento será definido pela simulação
            self.speedx = 0
            # Rotaciona a imagem utilizando o ângulo do corpo
            self.image = pygame.transform.rotate(self.orig_img, math.degrees(self.physical_block.angle))
            self.rect = self.image.get_rect()
            # Posiciona a imagem no centro de massa do corpo
            center = self.physical_block.position
            self.rect.centerx = center.x
            self.rect.centery = HEIGHT - center.y + self.camera_y
        # Condição caso o corpo ainda não tenha sido adicionado na simulação física
        else:
            self.rect.x += self.speedx
            # Rebate se chegar em uma das paredes (inverte o sinal da velocidade)
            if self.rect.left < 0 or self.rect.right > WIDTH:
                self.speedx = -self.speedx

class GameState:
    '''
    Classe responsável por analisar o estado do jogo, ou seja se os blocos cairam e colidiram
    Métodos - __init__, fell, blocks_collided   
    '''
    def __init__(self):
        ''' Construtor que inicia os atributos da classe'''
        self.running = True

    def fell(self, arbiter, space, data):
        '''
        Método que identifica o tipo de colisão e caso essa seja entre qualquer bloco (menos o primeiro) e o chão
        ele printa "Colidiu!" e o jogo para e vai para a tela Game Over

        argumentos:
        -self
        -arbiter: instância com as informações de colisão
        -space: espaço da simulação
        -data: informação
        '''
        for shape in arbiter.shapes: 
            if shape.collision_type == COLLTYPE_BLOCK:
                if shape.is_first: # Colidir menos quando for o primeiro
                    shape.in_building = True
                else:
                    print('Colidiu!')
                    self.running = False
        return True
    
    def blocks_collided(self, arbiter, space, data):
        ''' 
        Método que identifica a colisão entre dois blocos como válida

        Argumentos:
        - self: 
        - arbiter: instância com as informações de colisão
        - space: espaço da simulação
        - data: informação
        '''
        for shape in arbiter.shapes:
            shape.in_building = True
        return True
        
def gameover_screen(screen):
    ''' função responsável para criar a tela do game over, ou seja, a área onde a encerra o jogo e o jogador pode escolher se quer reiniciar ou sair do jogo
        argumentos:
        - screen: projeção da tela
        o que retorna - responsável por retornar a tela game over com os botões referentes aos blocos
    '''
    click = False
    while True:
        screen.blit(fundoinicial,(0,0)) # Projeta o fundo inicial, ou seja, aquele declarado da tela menu
        draw_text('GAME OVER', font, (255, 0, 0), screen, 110, 10) # Desenha o texto "GAME OVER"

        mx, my = pygame.mouse.get_pos() # Retorna a posição x e y do cursor do mouse

        button_1 = pygame.Rect(150, 200, 200, 50) 
        button_2 = pygame.Rect(150, 350, 200, 50)

        if button_1.collidepoint((mx, my)): # Condição caso o botão 1 seja clicado
            if click:
                return TELA_MENU # Retorna a tela menu

        if button_2.collidepoint((mx, my)): # Condição caso o botão 1 seja clicado
            if click:
                return SAIR # Retorna a tela menu


        pygame.draw.rect(screen, (0, 0, 0), button_1) # Desenha o retângulo (botão 1) na tela
        pygame.draw.rect(screen, (0, 0, 0), button_2) # Desenha o retângulo (botão 2) na tela
        draw_text('Reiniciar', font3, (255, 215, 0), screen, 195, 215) # Desenha "Reiniciar" na tela em cima do retângulo
        draw_text('Sair', font3, (255, 215, 0), screen, 222, 365) # Desenha "Sair" na tela em cima do retângulo
        draw_text("Que pena! Tente novamente", font3,  (0, 0, 0), screen, 90, 150) # Desenha "Que pena! Tente novamente" na tela em cima do retângulo
 
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

def game_screen(window, modo_jogo):
    ''' função responsável para criar a tela jogo, ou seja, a área onde a jogador poderá jogar
        argumentos:
        - window: janela na qual aparecerá a jogo
        - modo_jogo: qual modo de jogo
        o que retorna - retornar a tela jogo atualizada
    '''
    # Se o usuário escolher a tela jogo Mário
    if modo_jogo == TELA_JOGO_MARIO: 
        background = pygame.image.load('assets/imagens/fundo mario.png').convert() # Fundo Mário
        block_img = pygame.image.load('assets/imagens/bloco mario.png').convert_alpha() # Bloco Mário
        pygame.mixer.music.load('assets/sons/sommario.mp3') # Som do bloco caindo Mário
    # Se o usuário escolher a tela jogo Minecraft
    elif modo_jogo == TELA_JOGO_MINECRAFT:
        background = pygame.image.load('assets/imagens/fundo minecraft.png').convert() # Fundo Minecraft
        block_img = pygame.image.load('assets/imagens/bloco minecraft.jpg').convert_alpha() # Bloco Minecraft
        pygame.mixer.music.load('assets/sons/somminecraft.mp3') # Som do bloco caindo Minecraft
    # Se o usuário escolher a tela jogo Padrão
    elif modo_jogo == TELA_JOGO_NORMAL:
        background = pygame.image.load('assets/imagens/fundo.jpg').convert() # Fundo Padrão
        block_img = pygame.image.load('assets/imagens/block.png').convert_alpha() # Bloco Padrão
        pygame.mixer.music.load('assets/sons/somnormal.mp3') 
   
    block_img = pygame.transform.scale(block_img, (BLOCK_WIDTH, BLOCK_HEIGHT)) # Coloca o bloco em escala
    background = pygame.transform.scale(background,(WIDTH, HEIGHT)) # Coloca o fundo em escala

    recorde = carrega_recorde() 
    camera_y = 0 
    game = True
    clock = pygame.time.Clock() # Variável para o ajuste de velocidade
    FPS = 30 # Frame por segundo

    game_state = GameState()

    # Define espaço físico
    space = pymunk.Space()
    space.gravity = 0,-1000 # Define a gravidade da simulação
    space.sleep_time_threshold = 0.5
    # Define o chão (sem isso ele cai para sempre)
    floor = pymunk.Segment(space.static_body, (-WIDTH, 5), (2*WIDTH, 5), 5) # O chão é um segmento de reta que vai desde -WIDTH até 2*WIDTH
    floor.elasticity = 5  # Elasticidade do chão
    floor.friction = 10  # Coeficiente de atrito do chão
    floor.collision_type = COLLTYPE_FLOOR
    space.add(floor)  # Adiciona o chão na simulação
    handler = space.add_collision_handler(COLLTYPE_BLOCK, COLLTYPE_FLOOR)
    handler.begin = game_state.fell # Cair no chão
    handler = space.add_collision_handler(COLLTYPE_BLOCK, COLLTYPE_BLOCK)
    handler.begin = game_state.blocks_collided 

    speedx = 5 # Velocidade do bloco no eixo x

    # Criando um grupo de sprites
    all_sprites = pygame.sprite.Group()
    building = pygame.sprite.Group()
    last_block = Block(block_img, camera_y, speedx, True)
    all_sprites.add(last_block)
    font = pygame.font.SysFont(None, 48)

    contagem = pygame.time.get_ticks() # Contagem de tempo do pygame
    segundos = 120 # Define o tempo do jogo
    cont = 1000 # Contagem de 1000 milisegundos

    # Loop principal
    maior_altura = 0

    # Enquanto o jogo estiver rodando
    while game and game_state.running: 

        clock.tick(FPS) 

        # Trata eventos
        for event in pygame.event.get():
            # Verifica consequências
            if event.type == pygame.QUIT:
                game = False
                return SAIR
            if event.type == pygame.KEYDOWN:
                # Se o espaço foi apertado, adiciona o bloco na simulação física
                # Cria um novo bloco se movendo no topo da tela
                if event.key == pygame.K_SPACE:
                    last_block.add_physics(space)
                    building.add(last_block)
                    pygame.mixer.music.play(0)                   
                    last_block = Block(block_img, camera_y, speedx, False)
                    all_sprites.add(last_block)
                    pygame.mixer.music.play(0)

        for sprite in all_sprites:
            sprite.camera_y = camera_y
        
        expected_height = len(building) * BLOCK_HEIGHT # Altura necessária para subir a câmera y
        for block in building:
            height = HEIGHT - block.rect.top # A altura vai ser definida pelo comprimento da tela menos o topo do bloco
            # Condição de se o bloco estiver na torre e a altura da torre for maior que a maior alutra registrada
            if block.physical_shape.in_building and height > maior_altura: 
                maior_altura = height #A nova maior altura se torna a altura
        print('Altura: {0}, Recorde: {1}'.format(maior_altura, recorde))  # Printa a Altura e o Recorde com seus resectivos valores na tela    

        if maior_altura > recorde: # Condição de se a maior altura for maior que o recorde
            recorde = maior_altura # O recorde vai ser igual a maior altura atingida
            salva_recorde(recorde) # Salva o recorde na fução salva_recorde

        if maior_altura < 84: # Condição se a maior altura for menor que 210 pixels
            speedx = 7 # A velocidade do bloco é igual a 7 pixels por segundo

        elif maior_altura < 168 and maior_altura >= 84: # Condição se a maior altura estiver entre 210 e 378
            speedx = 10  # A velocidade do bloco é igual a 10 pixels por segundo
        
        elif maior_altura < 252 and maior_altura >= 168: # Condição se a maior altura estiver entre 376 e 672
            speedx = 13 # A velocidade do bloco é igual a 13 pixels por segundo
        
        elif maior_altura >= 316: # Condição se a maior altura for maior igual a 672
            speedx = 16 # A velocidade do bloco é igual a 16 pixels por segundo
        
        if expected_height - camera_y > 300: # Condição caso a subtração da altura esperada menos a camera y 
            camera_y += 1


        now = pygame.time.get_ticks()
        if (now - contagem > cont):
            segundos-=1
            cont+=1000

        # Atualiza estado do jogo
        # Atualizando a posição dos blocos
        all_sprites.update() # atualiza os sprites
        # Update physics
        dt = 1./FPS # Variação de tempo 
        space.step(dt) # Variação do espaço pela variação do tempo

        # Gera saídas
        window.blit(background,(0,0))   # Projeta o texto acima na tela 


        # Desenhando blocos
        all_sprites.draw(window)
        text = font2.render(f"Recorde: {recorde}", True, (0, 0, 0)) # Escreve "Recorde" e a maior altura de todos os jogos jogados
        window.blit(text, (10, 50)) #  Projeta o texto acima na tela 
        andares = font2.render(f"Altura: {maior_altura}", True, (0, 0, 0)) # Escreve "Altura" e a contagem da maior altura
        window.blit(andares, (10, 30))  # Projeta o texto acima na tela 

        if segundos < 0: # Condição se os segundos forem menor que zero
            return TELA_GAMEOVER # Retorna a tela game over
        else:
            text = font2.render(f"Timer: {segundos}", True, (0, 0, 0)) # Escreve "Timer" e a contagem regressiva dos segundos do jogo
            window.blit(text, (10, 10)) # Projeta o texto acima na tela 
        pygame.display.update()  # Mostra o novo frame para o jogador
    return TELA_GAMEOVER # Retorna a tela game over

tela_atual = TELA_MENU # declaração da tela atual igual a tela menu
while tela_atual != SAIR: # loop: enquanto a tela atual for diferente de sair...
    if tela_atual == TELA_MENU: # condição da tela atual igual a tela menu
        tela_atual = main_menu(screen) # tela atual igual à função main_menu(screen)
    elif tela_atual == TELA_OPTIONS: # condição da tela atual igual a tela opções
        tela_atual = options(screen) # tela atual igual à função options(screen)
    elif tela_atual == TELA_INSTRUCOES: # condição da tela atual igual a tela instruções
        tela_atual = instrucoes(screen) # tela atual igual à função instrucoes(screen)
    elif tela_atual in [TELA_JOGO_MARIO, TELA_JOGO_NORMAL, TELA_JOGO_MINECRAFT]: # condição da tela atual igual a tela do jogo mario, jogo normal, jogo minecraft
        tela_atual = game_screen(screen, tela_atual) # tela atual igual à função game_screen(screen)
    elif tela_atual == TELA_GAMEOVER: # condição da tela atual igual a tea do game over
        tela_atual = gameover_screen(screen) # tela atual igual à função gameover_screen(screen)

salva_recorde(0) # Zera recorde quando fechar o jogo
# Finalização
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
sys.exit() # Sair do Sistema 
