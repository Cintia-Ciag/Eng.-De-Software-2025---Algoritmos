#Nível 1 – Fundamentos
# 1. Busca Linear Simples
# Dado um vetor de números inteiros e um número alvo, use busca sequencial para
# verificar se o número está presente.
# Extra: informe o índice se encontrar.

def busca_sequecial(vetor, alvo):
    for (indice, numero) in enumerate(vetor):
        if numero == alvo:
            return indice
    return -1

vetor = [100, 20, 48, 200, 90]

num = int(input("Digite um numero: "))

Resultado = busca_sequecial(vetor, num)
print(Resultado)