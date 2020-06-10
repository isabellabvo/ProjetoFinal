def carrega_recorde():
    with open ("arquivo.json", "rb") as arquivo:
        configuracao = json.load(arquivo)
        recorde = configuracao["recorde"]
    return recorde

def salva_recorde(recorde):
    cash = {"recorde": recorde}
    with open ("arquivo.json", "w") as arquivo:
        arquivo.write(json.dumps(cash))
        print(json.dumps(cash))
        
def game_screen(window):
    recorde = carrega_recorde()
    expected_height = len(building) * BLOCK_HEIGHT
       # building_height = 0
       # print(f"B. Height: {building_height} || Exp. Height: {expected_height}")
       for block in building:
           height = HEIGHT - block.rect.top
           if block.physical_shape.in_building and height > maior_altura:
               maior_altura = height
       print('Maior altura: {0}, Recorde: {1}'.format(maior_altura, recorde))
       if maior_altura > recorde:
           recorde = maior_altura
           salva_recorde(recorde)
