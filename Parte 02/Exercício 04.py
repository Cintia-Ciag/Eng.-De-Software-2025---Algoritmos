# Busca linear

def busca_linear (lista, elemenio):
    for i in range (len(lista)):
        if lista [i] == elemento:
            return i
        else:
            return - 1
       
nomes = ["Ana", "Bruno", "Carlos", "Cintia", "Diego", "Fernanda"]

nome_procurado = input("Digite o nome que deseja procurar: ")

posicao = busca_linear(nomes, nome_procurado)

if posicao != - 1:
    print(f"O nome {nome_procurado} foi encontrado na posição {posicao}.")
else:
    print(f"O nome {nome_procurado} não foi encontrado na lista.")
    