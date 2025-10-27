# 1. Controle de Temperatura de Salas
# Contexto: Uma empresa monitora a temperatura de 5 salas, 3 vezes ao dia.
# Tarefa: Armazene as temperaturas em uma matriz 5x3. Calcule a temperatura média de cada sala.

temperaturas = []  

for i in range(5):  
    linha = []  
    for j in range(3):  
        temp = float(input(f"Digite a temperatura da sala {i+1}, medição {j+1}: ")) 
        linha.append(temp)
    temperaturas.append(linha)

for i in range(5):
    media = sum(temperaturas[i]) / 3
    print(f"A média da sala {i+1} é {media:.2f}°C")

print(temperaturas)