while game:
#Trata eventos
    for event in pygame.event.get():
        #Verifica consequências
        if event.type == pygame.QUIT:
            game = False

        if event.type == pygame.KEYUP:
            box = template_box.copy()
            box.body.position = 200, 100
            space1.add(box, box.body)
            
              ### Update physics
    fps = 60
    dt = 1./fps
    space1.step(dt)

# Gera saídas
    window.fill((0, 255, 0))  # Preenche com a cor branca
    #window.blit(fundo, (0, 0))
    #window.blit(bloco, (largura, altura))

    space1.debug_draw(draw_options1)
    window.blit(surf, (50,100))
