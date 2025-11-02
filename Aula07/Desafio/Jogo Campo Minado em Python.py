# Enunciado – Jogo Campo Minado em Python
# Objetivo
# Desenvolver um jogo simples de Campo Minado (Minesweeper) em Python, utilizando
# matrizes (listas bidimensionais) e funções para organizar o código.
# Descrição do Problema
# Você deverá implementar uma versão simplificada do Campo Minado em modo texto.
# O tabuleiro é representado por uma matriz, onde algumas posições contêm minas e as demais
# são espaços seguros.
# O jogador deve escolher coordenadas (linha e coluna) e tentar abrir as posições sem explodir
# uma mina.
# Regras do Jogo
# 1. O jogo começa com um tabuleiro oculto (exemplo: 5x5).
# 2. As minas são distribuídas aleatoriamente no tabuleiro.
# 3. O jogador escolhe posições digitando linha e coluna.
# 4. Se o jogador abrir:
# o Uma célula sem mina, ela mostra quantas minas há nas 8 posições vizinhas.
# o Uma célula com mina, o jogo termina ( Game Over).
# 5. O jogo termina quando:
# o O jogador abre todas as células seguras ( Vitória), ou
# o Explode uma mina ( Derrota).
# Requisitos Técnicos
# • O tabuleiro deve ser representado por uma matriz (lista de listas).
# • Devem ser usadas funções para modularizar o código, por exemplo:
# o criar_tabuleiro(linhas, colunas, qtd_minas)
# o mostrar_tabuleiro(tabuleiro, revelado)
# o contar_minas_vizinhas(tabuleiro, linha, coluna)
# o jogar(tabuleiro)
# • Use o módulo random para posicionar minas aleatoriamente.
# • Utilize try/except para tratar erros de entrada (ex: coordenadas inválidas).
# • O jogador deve ver o progresso a cada jogada.

import random

def criar_tabu(linhas, colunas, qtd_minas):
    print('\n*** CAMPO MINADO ***')
    print("Escolha linha e coluna para revelar células.")
    print("Evite as minas! Boa sorte!\n")
    
    tabuleiro = [[' ' for _ in range(colunas)] for _ in range(linhas)]
    
    minas_pos = 0
    while minas_pos < qtd_minas:
        l = random.randint(0, linhas - 1)
        c = random.randint(0, colunas - 1)
        if tabuleiro[l][c] == ' ':
            tabuleiro[l][c] = 'M'
            minas_pos += 1
    return tabuleiro

def mostrar_tabu(tabuleiro, revelado=False):
    print("\n" + "="*35)
    for i, linha in enumerate(tabuleiro):
        linha_visivel = []
        for cel in linha:
            if revelado:
                linha_visivel.append(cel if cel != ' ' else '.')
            else:
                if cel in '012345678':
                    linha_visivel.append(cel)
                elif cel == ' ':
                    linha_visivel.append('?')
                else:
                    linha_visivel.append('?')
        print(f"{i:2} | " + " | ".join(linha_visivel))
    print("    " + "   ".join(str(i) for i in range(len(tabuleiro[0]))))
    print("="*35)

def jogada(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            if 0 <= valor <= 4:
                return valor
            else:
                print("ERRO: Digite entre 0 e 4!")
        except ValueError:
            print("ERRO: Digite um número inteiro!")

def contar_minas(tabuleiro, linha, coluna):
    linhas, colunas = len(tabuleiro), len(tabuleiro[0])
    count = 0
    for dl in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dl == 0 and dc == 0:
                continue
            nl, nc = linha + dl, coluna + dc
            if 0 <= nl < linhas and 0 <= nc < colunas:
                if tabuleiro[nl][nc] == 'M':
                    count += 1
    return count

def jogar():
    
    tabuleiro = criar_tabu(5, 5, 6)
    
    linhas, colunas = 5, 5
    total_celulas = linhas * colunas
    minas = 6
    seguras = total_celulas - minas
    reveladas = 0

    while True:

        mostrar_tabu(tabuleiro)
        print(f"Células seguras restantes: {seguras - reveladas}\n")

        linha = jogada("Digite a LINHA (0-4): ")
        coluna = jogada("Digite a COLUNA (0-4): ")

        if tabuleiro[linha][coluna] not in [' ', 'M']:
            print("Célula já revelada! Tente outra.")
            continue

        if tabuleiro[linha][coluna] == 'M':
            print("\nBOOM! Você explodiu uma mina!")
            mostrar_tabu(tabuleiro, revelado=True)
            print("GAME OVER!")
            return False

        else:

            num = contar_minas(tabuleiro, linha, coluna)
            tabuleiro[linha][coluna] = str(num) if num > 0 else '.'
            reveladas += 1
            print(f"Célula segura! ({num} minas vizinhas)")

            if reveladas == seguras:
                print("\nPARABÉNS! Você venceu!")
                mostrar_tabu(tabuleiro, revelado=True)
                return True

jogar()