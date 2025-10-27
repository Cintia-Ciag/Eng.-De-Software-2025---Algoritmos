# 5. Registro de Pontos em Jogos
# Contexto: Uma liga de esportes registra pontos de 3 times em 4 jogos.
# Tarefa: Crie uma matriz 3x4 com os pontos e determine qual time teve maior pontuação total.

pontos = []
times = ["Time 1", "Time 2", "Time 3"]

for i in range(3):
    linha = []
    for j in range(4):
        ponto = int(input(f"\nDigite os pontos do {times[i]} no jogo {j+1}: "))
        linha.append(ponto)
    pontos.append(linha)

print("\n=*= Pontuações Totais =*=")
maior_pontuacao = 0
time_vencedor = ""
for i in range(3):
    total_time = sum(pontos[i])
    print(f"Total do {times[i]}: {total_time} pontos")
    if total_time > maior_pontuacao:
        maior_pontuacao = total_time
        time_vencedor = times[i]

print(f"\nO {time_vencedor} teve maior pontuação, com {maior_pontuacao} pontos!")

print("\nMatriz de pontos:", pontos)