SAIR = 0
TELA_MENU = 1
TELA_OPTIONS = 2
TELA_JOGO = 3
 
pygame.init() 
 
mainClock = pygame.time.Clock()
pygame.display.set_caption('Tower Blocks')
screen = pygame.display.set_mode((480, 600))
font = pygame.font.SysFont(None, 50)
fundoinicial = pygame.image.load("construcao.jpg").convert()
 
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
 
click = False
 
def main_menu(screen):
    click = False
    while True:
        screen.blit(fundoinicial,(0,0))
        draw_text('Menu principal', font, (255, 255, 255), screen, 20, 20)
 
        mx, my = pygame.mouse.get_pos()
 
        button_1 = pygame.Rect(50, 100, 200, 50)
        button_2 = pygame.Rect(50, 200, 200, 50)
 
        draw_text('Jogar', font, (255, 255, 255), screen, 200, 50)
       
        if button_1.collidepoint((mx, my)):
            if click:
                return TELA_JOGO
        if button_2.collidepoint((mx, my)):
            if click:
                return TELA_OPTIONS
        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)
 
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
 
def options(screen):
    click = False
    running = True
    while running:
 
        mx, my = pygame.mouse.get_pos()
        screen.fill((255,200,0))
        button1 = pygame.Rect(50, 100, 200, 50)
        button2 = pygame.Rect(50, 200, 200, 50)
        button3 = pygame.Rect(50, 300, 200, 50)
 
        pygame.draw.rect(screen, (255, 0, 0), button1)
        pygame.draw.rect(screen, (255, 0, 0), button2)
        pygame.draw.rect(screen, (255, 0, 0), button3)
 
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
 
        draw_text('Escolha o seu bloco!', font, (255, 255, 255), screen, 20, 20)
        
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
