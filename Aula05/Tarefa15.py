# Nível 3 – Desafios
# 14. Implementar sua própria função index()
# Crie uma função meu_index(lista, valor) que funcione como o método
# list.index(), usando busca sequencial.

def meu_index(lista, valor):
    for v in range(len(lista)):
        if lista[v] == valor: 
            return v      
    return -1

lista = [10, 20, 30, 40]
valor = 30
resultado = meu_index(lista, valor)
print(f"Índice de {valor}: {resultado}")