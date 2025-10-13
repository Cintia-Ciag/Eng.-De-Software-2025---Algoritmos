# Nível 2 – Aplicações Práticas
# 6. Busca de Nome em Lista
# Peça ao usuário para digitar nomes e depois procure um nome específico usando
# busca linear.

def busca_linear(lista_nomes, chave):
    for nome_consultado in lista_nomes:
        if nome_consultado == chave:
            print(f"O nome {nome_consultado} está na lista.")
            return nome_consultado
        else:
            print(f"O nome {nome_consultado} não está na lista.")
    return nome_consultado

lista_nomes = []

for nome in range(5):
    nome = str(input("Digite um nome: "))
    lista_nomes.append(nome)


nome_consultado = str(input("Digite o nome a ser consultado: "))

r = busca_linear(lista_nomes, nome_consultado)
print(r)