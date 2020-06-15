def carrega_recorde():
    ''' função responsável para guardar o número no arquivo json e se o anterior for menor que o número posterior, atualiza nesse arquivo
        argumentos - 
        o que retorna - responsável por retornar o recorde'''
    with open ("arquivo.json", "rb") as arquivo: # Abre o arquivo.json como um arquivo
        configuracao = json.load(arquivo) # Carrega o arquivo json
        recorde = configuracao["recorde"] # Escreve a string recorde no arquivo
    return recorde # Retorna o valor do maior número atingido (recorde)
