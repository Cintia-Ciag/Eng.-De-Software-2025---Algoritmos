# Nível 2 – Aplicações Práticas
# 8. Comparar Tempo de Execução
# Compare o tempo de execução da busca linear e busca binária em uma lista
# com 1 milhão de elementos. Use o módulo time.

import random
import time
import tracemalloc

tracemalloc.start()
inicio1 = time.time()

def buscalinear(lista, chave):
    for (indice, numero) in enumerate(lista):
        if numero == chave:
            return indice
    return -1

lista = [random.randint(1,1000000) for i in range(1000000)]
lista.sort()
print(lista)

final1 = time.time()

memoria_atual1,memoria_pico1 = tracemalloc.get_traced_memory()


tracemalloc.stop()


tracemalloc.start()
inicio2 = time.time()

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

final2 = time.time()

memoria_atual2,memoria_pico2 = tracemalloc.get_traced_memory()


tracemalloc.stop()

print(f"O tempo de execução eh:{final1-inicio1:.3f} segundos")
print(f"Memoria atual1 eh:{memoria_atual1/1024:.3f} segundos")
print(f"Pico Memoria1 eh:{memoria_pico1/1024:.3f} segundos")
print(f"O tempo de execução eh:{final2-inicio2:.3f} segundos")
print(f"Memoria atual2 eh:{memoria_atual2/1024:.3f} segundos")
print(f"Pico Memoria2 eh:{memoria_pico2/1024:.3f} segundos")