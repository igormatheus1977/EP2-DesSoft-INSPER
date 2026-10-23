from funcoes import *
from random import randint
frota = {}

nomes = [                                                                                                   # lista com o nome dos navios
    "porta-aviões",
    "navio-tanque",
    "contratorpedeiro",
    "submarino"
]

tamanhos = {                                                                                                # dicionarios com os tamanhos dos navios
    "porta-aviões":     4,                                                                                  # em que as chaves são seus nomes
    "navio-tanque":     3,                                                                                  # e os valores são seus tamanhos
    "contratorpedeiro": 2,
    "submarino":        1
}

quantidades = {                                                                                             # dicionarios com as quantidades de navios
    "porta-aviões":     1,                                                                                  # em que as chaves são seus nomes
    "navio-tanque":     2,                                                                                  # e os valores são suas quantidades
    "contratorpedeiro": 3,
    "submarino":        4
}

for navio in nomes:                                                                                         # para cada navio na lista 
    tamanho = tamanhos[navio]                                                                               # tamanho do navio analisado
    for i in range(quantidades[navio]):                                                                     # perguntar certinho a posição das quantidades exatas
        print(f'Insira as informações referentes ao navio {navio} que possui tamanho {tamanho}')            # pergunta do enunciado
        linha = int(input('Linha: '))                                                                       # pergunta do enunciado
        coluna = int(input('Coluna: '))                                                                     # pergunta do enunciado
        if navio != 'submarino':                                                                            # se o navio não for o submarino
            orientacao = int(input('[1] Vertical [2] Horizontal > '))
        else:
            orientacao = 1                                                                                  # ele pergunta qual a orientação

        if orientacao == 1:                                                                                 # se a orientação é 1, op será vertical
            op = 'vertical'                                                                                 #
        elif orientacao == 2:                                                                               # se a orientação é 2, op será horizontal
            op = 'horizontal'

        validacao_deu_green_ou_red = posicao_valida(frota, linha, coluna, op, tamanho)                      # verifica se a posição jogada é válida

        while validacao_deu_green_ou_red == False:                                                          # enquanto a posição é inválida:
            print('Esta posição não está válida!')                                                          # printa que é inválida
            print(f'Insira as informações referentes ao navio {navio} que possui tamanho {tamanho}')        # pergunta de novo
            linha = int(input("Linha: "))                                                                   # pergunta de novo
            coluna = int(input('Coluna: '))                                                                 # pergunta de novo
            if navio != 'submarino':                                                                        # se o navio não for submarino:
                orientacao = int(input("[1] Vertical [2] Horizontal > "))                                   # pergunta a orientação
            else:
                orientacao = 1                                                                              # se for submarino, deixa em 1
            if orientacao == 1:                                                                             # se orientação for 1
                op = 'vertical'                                                                             # op é vertical
            elif orientacao == 2:                                                                           # se orientação for 2
                op = 'horizontal'                                                                           # op é horizontal

            validacao_deu_green_ou_red = posicao_valida(frota, linha, coluna, op, tamanho)                  # verifica novamente e deixa o loop finito

        preenche_frota(frota, navio, linha, coluna, op, tamanho)

frota_oponente = {                                                                                          # frota oponente padrão fornecida pelos enunciados
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

tabuleiro_oponente = posiciona_frota(frota_oponente)                                                        # crio o tabuleiro do oponente
tabuleiro_jogador = posiciona_frota(frota)                                                                  # crio otabuleiro do jogador


jogando = True                                                                                              # variavel para o loop principal
while jogando == True:                                                                                      # enquanto ela é True:
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))                                          # printa o tabuleiro atual

    linha = int(input('Jogador, qual linha deseja atacar? '))                                               # pergunta a linha
    while linha < 0 or linha > 9:                                                                           # verificação se a linha
        print('Linha inválida!')                                                                            # atende os requisitos
        linha = int(input('Jogador, qual linha deseja atacar? '))                                           # pergunta novamente

    coluna = int(input('Jogador, qual coluna deseja atacar? '))                                             # pergunta a coluna
    while coluna < 0 or coluna > 9:                                                                         # verificação se a coluna
        print('Coluna inválida!')                                                                           # atende os requisitos
        coluna = int(input('Jogador, qual coluna deseja atacar? '))                                         # pergunta novamente

    while tabuleiro_oponente[linha][coluna] == 'X' or tabuleiro_oponente[linha][coluna] == '-':             # verifica se a jogada ja foi feita
        print(f"A posição linha {linha} e coluna {coluna} já foi informada anteriormente!")

        linha = int(input('Jogador, qual linha deseja atacar? '))                                           # novamente 
        while linha < 0 or linha > 9:                                                                       # faz
            print('Linha inválida!')                                                                        # a
            linha = int(input('Jogador, qual linha deseja atacar? '))                                       # verificação
 
        coluna = int(input('Jogador, qual coluna deseja atacar? '))                                         # novamente
        while coluna < 0 or coluna > 9:                                                                     # faz
            print('Coluna inválida!')                                                                       # a
            coluna = int(input('Jogador, qual coluna deseja atacar? '))                                     # verificação

    tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha, coluna)                                      # termina de criar o tabuleiro do oponente

    if afundados(frota_oponente, tabuleiro_oponente) == 10:                                                 # se o numero de navios afundados do oponente for 10,
        print('Parabéns! Você derrubou todos os navios do seu oponente!')                                   # o jogador ganha
        jogando = False                                                                                     # loop é encerrado

    else:                                                                                                   # se não...
        linha_oponente = randint(0, 9)                                                                      # sorteia a linha
        coluna_oponente = randint(0, 9)                                                                     # sorteia a coluna

        while tabuleiro_jogador[linha_oponente][coluna_oponente] == 'X' or tabuleiro_jogador[linha_oponente][coluna_oponente] == '-': 
            linha_oponente = randint(0, 9)                                                                  # se a linha sorteada for repetida, sorteia de novo
            coluna_oponente = randint(0, 9)                                                                 # se a coluna sorteada for repetida, sorteia de novo

        print(f'Seu oponente está atacando na linha {linha_oponente} e coluna {coluna_oponente}')           # fala onde o oponente está atacando

        tabuleiro_jogador = faz_jogada(tabuleiro_jogador, linha_oponente, coluna_oponente)                  # atualiza o tabuleiro do jogador

        if afundados(frota, tabuleiro_jogador) == 10:                                                       # se o numero de navios afundados do jogador for 10
            print('Xi! O oponente derrubou toda a sua frota =(')                                            # o jogador perde
            jogando = False                                                                                 # loop é encerrado