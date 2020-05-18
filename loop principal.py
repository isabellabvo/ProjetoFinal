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
