# Considere as atividades da Lista 2(aula anterior)

# Caso4: Análise de Vendas Mensais
# Caso6: Sistema de Biblioteca
# Implemente os códigos usando Dicionários.

#Caso4: Análise de Vendas Mensais 
#Uma loja online registra o número de vendas de cada dia do mês em uma lista. 
#• Exemplo: [10, 15, 20, 5, 0, 8, ...] 
#O gerente precisa: 
#1. Calcular o total de vendas no mês. 
#2. Descobrir o dia com mais vendas e o dia com menos vendas. 
#3. Calcular a média de vendas por dia. 
#4. Listar os dias que tiveram vendas acima da média. 

print("\n***Análise de Vendas Mensais\n***")

vendas={
    "dia 1":20,
    "dia 2":50,
    "dia 3":466,
    "dia 4":478,
    "dia 5":256,
    "dia 6":145,
    "dia 7":1456,
      }
for chave, valor in vendas.items():
    print(chave, valor)


total = sum(vendas.values())

dmaisvendas = max(vendas, key=vendas.get)
dmenosvendas = min(vendas, key=vendas.get)

mediav = total/ len(vendas)

dam = [d for d, qtd in vendas.items() if qtd > mediav] 

print("\n ---Resultado da Análise---\n")
print(f"O total de vendas: {total}")
print(f"O dia com mais vendas: {dmaisvendas}")
print(f"O dia com menos vendas: {dmenosvendas}")
print(f"A média de vendas: {mediav}")
print(f"Os dias com vendas acima da média: {dam}\n")