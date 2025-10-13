# Nível 2 – Aplicações Práticas
# 7. Busca Binária Recursiva
# Implemente a versão recursiva da busca binária em uma lista ordenada.

def busaca_Binaria_recursiva(lista, chave):
    inicio = 0
    fim = len(lista) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == chave:
            return meio
        if lista[meio] > chave:
            fim = meio -1
        if lista[meio] < chave:
            inicio = meio + 1
    return -1

lista = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

resultado = busaca_Binaria_recursiva(lista,35)
print(resultado)