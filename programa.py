from funcoes import *
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

frota_oponente = {
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

tabuleiro_oponente = posiciona_frota(frota_oponente)
tabuleiro_jogador = posiciona_frota(frota)


jogando = True
while jogando == True:
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))

    linha = int(input('Jogador, qual linha deseja atacar? '))
    while linha < 0 or linha > 9:
        print('Linha inválida!')
        linha = int(input('Jogador, qual linha deseja atacar? '))

    coluna = int(input('Jogador, qual coluna deseja atacar? '))
    while coluna < 0 or coluna > 9:
        print('Coluna inválida!')
        coluna = int(input('Jogador, qual coluna deseja atacar? '))

    while tabuleiro_oponente[linha][coluna] == 'X' or tabuleiro_oponente[linha][coluna] == '-':
        print(f"A posição linha {linha} e coluna {coluna} já foi informada anteriormente!")

        linha = int(input('Jogador, qual linha deseja atacar? '))
        while linha < 0 or linha > 9:
            print('Linha inválida!')
            linha = int(input('Jogador, qual linha deseja atacar? '))
 
        coluna = int(input('Jogador, qual coluna deseja atacar? '))
        while coluna < 0 or coluna > 9:
            print('Coluna inválida!')
            coluna = int(input('Jogador, qual coluna deseja atacar? '))

    tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha, coluna)

    if afundados(frota_oponente, tabuleiro_oponente) == 10:
        print('Parabéns! Você derrubou todos os navios do seu oponente!')

        jogando = False