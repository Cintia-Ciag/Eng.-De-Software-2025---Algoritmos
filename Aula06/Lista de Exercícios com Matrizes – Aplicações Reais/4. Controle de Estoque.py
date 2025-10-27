# 4. Controle de Estoque
# Contexto: Uma loja possui 4 produtos e verifica o estoque em 3 lojas diferentes.
# Tarefa: Crie uma matriz 4x3 com as quantidades de cada produto em cada loja e calcule o total
# de cada produto.

estoque = []
lojas = ["Loja 1", "Loja 2", "Loja 3"]
produtos = ["Produto 1", "Produto 2", "Produto 3", "Produto 4"]

for i in range(4):
    linha = []
    for j in range(3):
        quantidade = int(input(f"\nDigite a quantidade de {produtos[i]} na {lojas[j]}: "))
        linha.append(quantidade)
    estoque.append(linha)

print("\n***Totais por Produto ***")
for i in range(4):
    total_produto = sum(estoque[i])
    print(f"Total de {produtos[i]}: {total_produto} unidades")

print("\nMatriz de estoque:", estoque)