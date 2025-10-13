# Nível 3 – Desafios
# 13. Buscar Produtos por Preço
# Dada uma lista de produtos com preços, implemente uma busca para encontrar todos os
# produtos com um determinado preço.

produtos = [  # Lista de tuplas (nome, preço)
    ("Biscoito", 5.0),
    ("Banana", 3.0),
    ("Maçã", 5.0),
    ("Refri", 4.0)
]

def buscar_Produtos(produtos, preco_procurar):
    inicio = 0
    fim = len(produtos) -1
    resultado = -1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if produtos[meio] == preco_procurar:
            resultado =  meio
            fim = meio -1
        elif produtos[meio] < preco_procurar:
            inicio = meio +1
        else:
            fim = meio -1
            return resultado


preco_procurar = 5.0
resultado = buscar_Produtos(produtos, preco_procurar)
print(resultado)