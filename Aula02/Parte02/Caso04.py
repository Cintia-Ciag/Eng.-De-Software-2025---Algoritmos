#Caso4: Análise de Vendas Mensais 
#Uma loja online registra o número de vendas de cada dia do mês em uma lista. 
#• Exemplo: [10, 15, 20, 5, 0, 8, ...] 
#O gerente precisa: 
#1. Calcular o total de vendas no mês. 
#2. Descobrir o dia com mais vendas e o dia com menos vendas. 
#3. Calcular a média de vendas por dia. 
#4. Listar os dias que tiveram vendas acima da média. 

print("\n***ANÁLISE DE VENDAS MENSAIS***\n")

for i in range(31):
    vendas=input(f"Digite a venda do dia {i+1}°: ")
    ven=[int(v) for v in vendas.split()]

total = sum(ven)

dmaisvendas = vendas.index(max(vendas))+1
dmenosvendas = vendas.index(min(vendas))+1

mediav = total/ len(vendas)

dam = [v for v in ven if v > mediav]

print("\n ---Resultado da Análise---\n")
print(f"O total de vendas: {total}")
print(f"O dia co mais vendas: {dmaisvendas}")
print(f"O dia com menos vendas: {dmenosvendas}")
print(f"A média de vendas: {mediav}")
print(f"Os dias com vendas acima da média: {dam}\n")