# Busca linear

def busca_linear (nomes, nome_procurado):
    for i in range (len(nomes)):
        if nomes [i] == nome_procurado:
            return i
       
nomes = ["Ana", "Bruno", "Carlos", "Cintia", "Diego", "Fernanda"]

nome_procurado = input("\nDigite o nome que deseja procurar: ")

posicao = busca_linear(nomes, nome_procurado)

if posicao != - 1:
    print(f"O nome {nome_procurado} foi encontrado na posição {posicao}.")
else:
    print(f"O nome {nome_procurado} não foi encontrado na lista.")
