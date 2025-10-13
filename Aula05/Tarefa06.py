#Nível 1 – Fundamentos
# 5. Verificar Elemento (Busca Binária)
# o Dada uma lista ordenada, implemente a busca binária para verificar se o
# elemento existe.

lista_nome = ["Ana", "bia", "cintia"]

def busca_linear(lista_nome, chave):
    indice = 0
    for nome in lista_nome:
        if nome == chave:
            print(f"O nome consultado {nome}, se encontra na posição {indice}")
            return indice
        indice = indice + 1
    return -1

nome = str(input("Digita o nome que deseja consultar: "))

r = busca_linear(lista_nome, nome)
print(r)
