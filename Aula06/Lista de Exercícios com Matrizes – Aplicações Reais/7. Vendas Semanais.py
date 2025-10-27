# 7. Vendas Semanais
# Contexto: Uma cafeteria registra vendas de 5 produtos durante 7 dias.
# Tarefa: Armazene os valores em uma matriz 5x7 e calcule a receita total semanal de cada
# produto.

vendas = []
produtos = ["Café", "Pão", "Bolo", "Suco", "Torta"]
dias = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sab", "Dom"]

for i in range(5):
    linha = []
    for j in range(7):
        venda = float(input(f"\nDigite a venda de {produtos[i]} no dia {dias[j]} (em R$): "))
        linha.append(venda)
    vendas.append(linha)

print("\n=*= Receita Total Semanal por Produto =*=")
for i in range(5):
    receita_total = sum(vendas[i])
    print(f"\nReceita total de {produtos[i]}: R${receita_total:.2f}")

print("\nMatriz de vendas:", vendas)