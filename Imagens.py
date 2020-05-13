#Fundo
largura = 100
altura = 50
imagemdobloco = pygame.image.load('C:\\Users\\55119\\Desktop\\insper\\dessoft\\Square_34544.png').convert()
bloco = pygame.transform.scale(imagemdobloco, (largura, altura))
imagemfundo = pygame.image.load('assets/img/starfield.png').convert()
fundo = pygame.transform.scale(imagemfundo, (WIDTH, HEIGHT))
