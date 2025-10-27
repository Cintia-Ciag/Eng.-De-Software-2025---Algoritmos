# 8. Distribuição de Cadeiras
# Contexto: Uma sala de cinema tem 5 filas com 6 cadeiras cada.
# Tarefa: Crie uma matriz 5x6 e marque quais cadeiras estão ocupadas com “X” e quais estão
# livres com “O”

cadeiras = []


for i in range(5):
    linha = []
    for j in range(6):
        status = input(f"\nDigite o status da cadeira na fila {i+1}, cadeira {j+1} (X para ocupada, O para livre): ")
        linha.append(status)
    cadeiras.append(linha)

print("\n*** Distribuição de Cadeiras na Sala de Cinema ***")
for i in range(5):
    print(f"Fila {i+1}: {' '.join(cadeiras[i])}")
    
print("\nMatriz de cadeiras:", cadeiras)