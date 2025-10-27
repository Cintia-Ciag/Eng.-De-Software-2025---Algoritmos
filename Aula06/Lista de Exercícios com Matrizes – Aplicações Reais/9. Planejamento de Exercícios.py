# 9. Planejamento de Exercícios
# Contexto: Uma academia planeja 3 tipos de exercícios para 4 alunos diferentes.
# Tarefa: Crie uma matriz 4x3 que registre quantas repetições cada aluno deve fazer e calcule o
# total de repetições de cada exercício.

repeticoes = []
alunos = ["Aluno 1", "Aluno 2", "Aluno 3", "Aluno 4"]
exercicios = ["Agachamento", "Afundo", "Abdominal"]

for i in range(4):
    linha = []
    for j in range(3):
        reps = int(input(f"\nDigite as repetições de {exercicios[j]} para {alunos[i]}: "))
        linha.append(reps)
    repeticoes.append(linha)

print("\n=*= Total de Repetições por Exercício =*=")
for j in range(3):
    total_exercicio = sum(repeticoes[i][j] for i in range(4))
    print(f"\nTotal de {exercicios[j]}: {total_exercicio} repetições")

print("\nMatriz de repetições:", repeticoes)