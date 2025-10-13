# Nível 2 – Aplicações Práticas
# 9. Encontrar Primeira Ocorrência (Busca Binária Modificada)
# Dada uma lista ordenada com elementos repetidos, use busca binária modificada
# para encontrar o índice da primeira ocorrência de um número.

def busca_binaria_modificada(lista, alvo):
    inicio = 0
    fim = len(lista) -1
    resultado = -1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == alvo:
            resultado =  meio
            fim = meio -1
        elif lista[meio] <alvo:
            inicio = meio +1
        else:
            fim = meio -1
            return resultado
        
lista = sorted([1, 2, 3, 4, 4, 4, 5, 6, 7, 8, 9])
alvo = int(input("Qual número: "))
resultado = busca_binaria_modificada(lista, alvo)
print(f"Primeira Ocorrência {alvo} em {resultado}.")