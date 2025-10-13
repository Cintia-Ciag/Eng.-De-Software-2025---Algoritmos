# Tarefa 1 - Compare o tempo de execução e uso de memória para algoritmos de busca sequencial e binária.
# Para o teste considere uma lista de 1000 000 de elementos inteiros e randômicos.

import random
import time
import tracemalloc
tracemalloc.start()
inicio = time.time()

def buscaSequencial(lista, chave):
    for (indice, numero) in enumerate(lista):
        if numero == chave:
            return indice
    return -1

def buscaBinária(lista, chave):
    pos_ini = 0
    pos_fim = len(lista) - 1
    while pos_ini <= pos_fim:
        pos_meio = (pos_ini + pos_fim) // 2
        if lista[pos_meio] == chave:
            return pos_meio
        if lista[pos_meio] > chave:
            pos_fim = pos_meio - 1
        else:
            pos_ini = pos_meio + 1
        return -1

lista = [random.randint(1,1000000) for i in range(1000000)]
lista.sort()
print(lista)

final = time.time()

memoria_atual,memoria_pico = tracemalloc.get_traced_memory()


tracemalloc.stop()

print(f"O tempo de execução eh:{final-inicio:.3f} segundos")
print(f"Memoria atual eh:{memoria_atual/1024:.3f} segundos")
print(f"Pico Memoria eh:{memoria_pico/1024:.3f} segundos")


resultado1= buscaSequencial(lista,35)
print(resultado1)
resultado2 = buscaBinária(lista,35)
print(resultado2)