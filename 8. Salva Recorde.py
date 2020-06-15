def salva_recorde(recorde):
    ''' função responsável para guardar o maior número da função carrega_recorde
        argumentos: 
        - recorde: maior número gerado pelo jogador
        o que retorna - responsável por retornar o print do recorde'''
    cash = {"recorde": recorde} # Adiciona o valor do recorde como um value em um dicionário no arquivo
    with open ("arquivo.json", "w") as arquivo:
        arquivo.write(json.dumps(cash)) # Transforma de volta para JSON
        print(json.dumps(cash)) 
