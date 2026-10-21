def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []

    for i in range(tamanho):
        if orientacao == 'vertical':
            posicoes.append([linha + i, coluna])
        else:
            posicoes.append([linha, coluna + i])

    return posicoes

def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)

    if nome_navio in frota:
        frota[nome_navio].append(posicoes)
    else:
        frota[nome_navio] = [posicoes]

    return frota

def faz_jogada(tabuleiro, linha, coluna):
    tabuleiro_novo = tabuleiro
    
    if tabuleiro[linha][coluna] == 1:
        tabuleiro_novo[linha][coluna] = 'X'
    elif tabuleiro[linha][coluna] == 0:
        tabuleiro_novo[linha][coluna] = '-'

    return tabuleiro_novo