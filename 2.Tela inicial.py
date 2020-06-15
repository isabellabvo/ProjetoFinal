#Tela Inicial

#Mudança do ícone do jogo
programIcon = pygame.image.load('logo.png')
pygame.display.set_icon(programIcon)

#Definição de diferentes telas como variáveis
SAIR = 0
TELA_MENU = 1
TELA_OPTIONS = 2
TELA_JOGO_MARIO = 3
TELA_JOGO_MINECRAFT = 4
TELA_JOGO_NORMAL = 5
TELA_INSTRUCOES = 6
TELA_GAMEOVER = 7

#Inicialização do pygame
pygame.init()

mainClock = pygame.time.Clock() #Cria uma variável responsável pelo tempo
pygame.display.set_caption('Tower Blocks') #Define o título da janela
screen = pygame.display.set_mode((480, 600)) #Dimensões da janela
font = pygame.font.SysFont("Bauhaus 93", 50) #Cria variável para guardar a fonte "Bauhaus 93" de tamanho 50
font2 = pygame.font.SysFont(None, 25) #Cria variável para guardar a fonte padrão de tamanho 25
font3 = pygame.font.SysFont(None, 35) #Cria variável para guardar a fonte padrão de tamanho 35
font4 = pygame.font.SysFont("Bauhaus 93", 45) #Cria variável para guardar a fonte "Bauhaus 93" de tamanho 45
fundoinicial = pygame.image.load("construcao.jpg").convert() #Guarda imagem de fundo das telas menu, gameover e instruções

