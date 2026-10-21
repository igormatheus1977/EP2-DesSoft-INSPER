def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []

    for i in range(tamanho):                           # pega o tamanho do naviç
        if orientacao == 'vertical':                   # se for verticial:
            posicoes.append([linha + i, coluna])       # vê a linha i+1
        if orientacao == 'horizontal':                 # se for horizontal:
            posicoes.append([linha, coluna + i])       # vê a coluna j+1

    return posicoes

def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)      # reciclo a função anterior e defino posicoes do navio

    if nome_navio in frota:                                             # se o navio ja tiver na frota, eu adiciono a posição dele 
        frota[nome_navio].append(posicoes)
    else:
        frota[nome_navio] = [posicoes]                                  # senão, eu faço uma lista, pq quando voltar, o navio ja existirá e basta adiocionar com o append anterior

    return frota

def faz_jogada(tabuleiro, linha, coluna):
    tabuleiro_novo = tabuleiro                         # cria um novo tabuleiro cópia
    
    if tabuleiro[linha][coluna] == 1:
        tabuleiro_novo[linha][coluna] = 'X'            # se o elemento for igual a 1: 1 -> "X"
    elif tabuleiro[linha][coluna] == 0:
        tabuleiro_novo[linha][coluna] = '-'            # se o elemento for igual a 0: 0 -> "-"

    return tabuleiro_novo

def posiciona_frota(frota):
    tabuleiro = [
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],                      # tabuleiro 10x10
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    for navios in frota.values():                      # para um navio dentro do dicionario frotas,
        for posicao in navios:                         # para uma posição de um navio dentro da frota,
            for linha, coluna in posicao:              # para uma linha e uma coluna dentro da posição do navio dentro da frota,
                tabuleiro[linha][coluna] = 1           # o tabuleiro na posição linha x coluna, virará 1

    return tabuleiro                                   # retorna o tabuleiro preenchido

def afundados(frota, tabuleiro):
    counter = 0                                        # inicia a contabilização

    for navios in frota.values():                      # para um návio dentro do frotas
        for posicoes in navios:                        # para uma posição dentro do návio
            acertos = 0                                # o codigo acertou 0 vezes 
            for linha, coluna in posicoes:             # para uma linha e uma coluna dentro dessa poição:
                if tabuleiro[linha][coluna] == "X":    # se o tabuleiro na linha x coluna for = x
                    acertos += 1                       # o acerto é adicionado em 1
            if acertos == len(posicoes):               # se o numero de acertos for igual ao 
                counter += 1                           # tamanho do návio, counter é adicionado 1
    return counter

