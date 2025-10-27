# 2. Grade de Notas de Alunos
# Contexto: Uma turma de 4 alunos realizou 3 provas.
# Tarefa: Armazene as notas em uma matriz 4x3 e calcule a média de cada aluno e a média de
# cada prova.

notas = []

for i in range(4):
    linha = []
    for j in range(3):
        nota = float(input(f"Digite a nota do aluno {i+1} na prova {j+1}: "))
        linha.append(nota)
    notas.append(linha)

print("\nMédias dos alunos:")
for i in range(4):
    media_aluno = sum(notas[i]) / 3
    print(f"Aluno {i+1}: {media_aluno:.2f}")

print("\nMédias das provas:")
for j in range(3):
    soma_prova = sum(notas[i][j] for i in range(4))
    media_prova = soma_prova / 4
    print(f"Prova {j+1}: {media_prova:.2f}")

print("\nMatriz de notas:", notas)