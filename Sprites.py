#Fundo padrão
fundoinicial = pygame.image.load("construcao.jpg").convert()
#Bloco Mario
blocomario = pygame.image.load("bloco mario.png").convert()
blocomario = pygame.transform.scale(blocomario, (100, 100))
#Bloco Minecraft
blocominecraft = pygame.image.load("bloco minecraft.jpg").convert()
blocominecraft = pygame.transform.scale(blocominecraft, (100, 100))
#Bloco Padrão
bloconormal = pygame.image.load("block.png").convert()
bloconormal = pygame.transform.scale(bloconormal, (130, 80))

block_img = pygame.image.load('block.png').convert_alpha()
block_img = pygame.transform.scale(block_img, (BLOCK_WIDTH, BLOCK_HEIGHT))

#checar o bloco padrão e qual a gente vai usar
