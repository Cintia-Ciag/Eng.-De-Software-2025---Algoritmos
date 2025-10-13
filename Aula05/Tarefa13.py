# Nível 3 – Desafios
# 12. Jogo: Adivinhe o Número (Busca Binária)
# O computador escolhe um número entre 1 e 100. O jogador tenta adivinhar, e o
# computador responde se é maior ou menor. Use lógica de busca binária para resolver
# com o menor número de tentativas.

import random

def busca_binaria(numero_secreto, adivinhar):
    tentativas = 0
    inicio = 1
    fim = 100
    while inicio <= fim:  
        meio = (inicio + fim) // 2
        meio == adivinhar
        tentativas += 1
        if meio == numero_secreto:
            print(f"Adivinhado em {tentativas} tentativas: {meio}")
            break
        elif meio < numero_secreto:
            inicio = meio + 1  
        else:
            fim = meio - 1  
    else:
        print("Não achou")  


numero_secreto = random.randint(1, 100)  
adivinhar = int(input("Adivinhe um número: "))
resultado = busca_binaria(numero_secreto,adivinhar)
print(resultado)