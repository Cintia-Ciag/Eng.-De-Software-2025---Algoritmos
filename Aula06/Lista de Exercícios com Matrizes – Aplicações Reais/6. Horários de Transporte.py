# 6. Horários de Transporte
# Contexto: Um ponto de ônibus tem 4 linhas, cada uma com 3 horários.
# Tarefa: Armazene os horários em uma matriz 4x3 e permita que o usuário consulte os horários
# de uma linha específica.

horarios = []
linhas = ["Linha 1", "Linha 2", "Linha 3", "Linha 4"]

for i in range(4):
    linha = []
    for j in range(3):
        horario = input(f"\nDigite o {j+1}° horário da {linhas[i]} (ex.: 07:00): ")
        linha.append(horario)
    horarios.append(linha)

linha_consulta = int(input("\nDigite o número da linha para consultar (1 a 4): ")) - 1
if 0 <= linha_consulta < 4:
    print(f"\nHorários da {linhas[linha_consulta]}:")
    for j in range(3):
        print(f"Horários {j+1}: {horarios[linha_consulta][j]}")
else:
    print("\nLinha inválida! Escolha entre 1 e 4.")

print("\nMatriz de horários:", horarios)