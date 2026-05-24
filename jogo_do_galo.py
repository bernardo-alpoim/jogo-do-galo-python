import random

print('''Bem-vindo ao Jogo do Galo!
As posições são numeradas de 1 a 9:
 1 | 2 | 3 
-----------
 4 | 5 | 6 
-----------
 7 | 8 | 9''')

vitorias = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
tabuleiro = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
vencedor = False

simbolo = input('Com que símbolo quer jogar, "X" ou "O"?: ').upper()
if simbolo == 'X':
    simbolo_computador = 'O'
else:
    simbolo_computador = 'X'

def imprimir_tabuleiro(tabuleiro):
    print(f" {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]} ")
    print("-----------")
    print(f" {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]} ")
    print("-----------")
    print(f" {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]} ")

def jogada_utilizador(tabuleiro, simbolo):
    while True:
        try:
            posicao = int(input('Faça a sua jogada (1-9): '))
            if posicao in range(1, 10) and tabuleiro[posicao - 1] == ' ':
                tabuleiro[posicao - 1] = simbolo
                break
            else:
                print('Jogada inválida! Tenta outra vez.')
        except ValueError:
            print('Por favor, introduz um número válido de 1 a 9.')

def jogada_computador(tabuleiro, simbolo_computador, simbolo):
    for combinacao in vitorias:
        simbolos = [tabuleiro[i] for i in combinacao]
        if simbolos.count(simbolo_computador) == 2 and ' ' in simbolos:
            posicao = combinacao[simbolos.index(' ')]
            tabuleiro[posicao] = simbolo_computador
            return
    for combinacao in vitorias:
        simbolos = [tabuleiro[i] for i in combinacao]
        if simbolos.count(simbolo) == 2 and ' ' in simbolos:
            posicao = combinacao[simbolos.index(' ')]
            tabuleiro[posicao] = simbolo_computador
            return
    if tabuleiro[4] == ' ':
        tabuleiro[4] = simbolo_computador
        return
    
    for canto in [0, 2, 6, 8]:
        if tabuleiro[canto] == ' ':
            tabuleiro[canto] = simbolo_computador
            return
    casas_livres = []
    for i in range(9):
        if tabuleiro[i] == ' ':
            casas_livres.append(i)
    posicao = random.choice(casas_livres)
    tabuleiro[posicao] = simbolo_computador

def verificar_vitoria(tabuleiro, simbolo):
    for combinacao in vitorias:
        if tabuleiro[combinacao[0]] == tabuleiro[combinacao[1]] == tabuleiro[combinacao[2]] == simbolo:
            return True
    return False

while ' ' in tabuleiro and not vencedor:
    imprimir_tabuleiro(tabuleiro)
    jogada_utilizador(tabuleiro, simbolo)
    if verificar_vitoria(tabuleiro, simbolo):
        vencedor = True
        imprimir_tabuleiro(tabuleiro)
        print('Ganhaste!')
    elif ' ' in tabuleiro:
        jogada_computador(tabuleiro, simbolo_computador, simbolo)
        if verificar_vitoria(tabuleiro, simbolo_computador):
            vencedor = True
            imprimir_tabuleiro(tabuleiro)
            print('Perdeste!')

if not vencedor:
    imprimir_tabuleiro(tabuleiro)
    print('Empate!')
