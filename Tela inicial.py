#Tela Inicial

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
