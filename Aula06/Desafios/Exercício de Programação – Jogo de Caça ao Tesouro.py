# Exercício de Programação – Jogo de Caça ao
# Tesouro
# Objetivo
# Desenvolver um programa em Python que simule um jogo de caça ao tesouro utilizando matrizes
# (listas bidimensionais). O objetivo é praticar conceitos de listas, loops, entrada de dados e
# condicionais, implementando um jogo funcional que interaja com o usuário pelo terminal.
# Descrição do Problema
# Você deverá criar um programa que:
# 1. Crie um tabuleiro representado por uma matriz 5x5.
# 2. Posicione um tesouro em uma posição aleatória do tabuleiro.
# 3. Permita que o jogador faça 7 tentativas para encontrar o tesouro.
# 4. Para cada tentativa, o jogador deve informar:
# o Linha (0 a 4)
# o Coluna (0 a 4)
# 5. Caso o jogador acerte a posição do tesouro:
# o Marque a posição no tabuleiro com "T".
# o Exiba uma mensagem de vitória e finalize o jogo.
# 6. Caso o jogador erre:
# o Marque a posição escolhida com "X".
# o Informe uma dica indicando se o tesouro está mais para cima, baixo, esquerda ou
# direita.
# 7. Ao final das tentativas, caso o tesouro não seja encontrado, exiba a posição correta.
# 8. Exiba o tabuleiro atualizado após cada tentativa.
# Regras e Restrições
# • Use listas bidimensionais para representar o tabuleiro.
# • O programa deve rodar no terminal; não utilize bibliotecas gráficas.
# • As posições do tabuleiro são numeradas de 0 a 4 para linhas e colunas.
# • Não permita que o jogador insira valores fora do tabuleiro.
# • Evite qualquer comportamento que quebre a execução do programa (como entradas
# inválidas).
# Exemplo de Execução
# === Tabuleiro ===
# ~ ~ ~ ~ ~
# ~ ~ ~ ~ ~
# ~ ~ ~ ~ ~
# ~ ~ ~ ~ ~
# ~ ~ ~ ~ ~
# Tentativa 1 de 7
# Escolha a linha (0-4): 2
# Escolha a coluna (0-4): 3
# O tesouro está mais para baixo e mais para a esquerda.
# === Tabuleiro ===
# ~ ~ ~ ~ ~
# ~ ~ ~ ~ ~
# ~ ~ ~ X ~
# ~ ~ ~ ~ ~
# ~ ~ ~ ~ ~
# Avaliação
# • Implementação correta do tabuleiro e matrizes: 3 pontos
# • Registro correto das tentativas e marcações: 2 pontos
# • Dicas fornecidas corretamente: 2 pontos
# • Tratamento de entradas inválidas: 1 ponto
# • Código legível e organizado: 2 pontos
# Total: 10 pontos

import random

tabuleiro = [['~'for _ in range(5)] for _ in range(5)]

linha = random.randint(0, 4)
coluna = random.randint(0, 4)

tentativas = 7
tentativa_atual = 1

def tabu():

    # for l in range(1, tentativa_atual +1):
        print('\n***TABULEIRO***')
        for l in tabuleiro:
            print(' '.join(l))

def jogada(mensagem):  
    while True:
        try:
            posicao = int(input(mensagem))
            if 0 <= posicao <= 4:
                return posicao
            else:
                print('ERRO: Digite um número entre 0 e 4.')
        except ValueError:
            print('ERRO: Digite um número inteiro válido.')

def dica(horizontal, vertical):
    dicas = []
    if horizontal < linha:
        dicas.append('mais para baixo')
    elif horizontal > linha:
        dicas.append('mais para cima')
    if  vertical < coluna:
        dicas.append('mais para direita')
    elif vertical > coluna:
        dicas.append('mais para a esquerda')
    if dicas:
        if len(dicas) == 1:
            print(f'\nO tesouro está {dicas[0]}.')  
        else:
             print(f'\nO tesouro está {' e '.join(dicas)}.')

while tentativa_atual <= tentativas:
    tabu()
    print(f'\nTentativa {tentativa_atual} de {tentativas}\n')
    posiçao1 = jogada('Escolha a posição (0-4) na horizontal: ')
    posiçao2 = jogada('Escolh a posição (0-4) na vertical: ')

    if tabuleiro[posiçao1][posiçao2] == 'X':
        print('\nVocê já tentou está posição. Escolha outra posição: ')
        continue

    if posiçao1 == linha and posiçao2 == coluna:
        tabuleiro[posiçao1][posiçao2] = 'T'
        tabu()
        print(f'Parabéns! Você encontrou o tesouro escondindo na tentativa, {tentativa_atual}.')
        break

    tabuleiro[posiçao1][posiçao2] = 'X'
    dica(posiçao1, posiçao2)
    tentativa_atual += 1

if tentativa_atual > tentativas:
    tabuleiro[linha][coluna] = 'T'
    tabu()
    print(f"\nFim de jogo! O tesouro estava na posição ({linha}, {coluna}).\n")
