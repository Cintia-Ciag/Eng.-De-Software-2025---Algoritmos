# 3. Agenda Semanal
# Contexto: Um consultório possui 5 dias de atendimento e 3 horários por dia.
# Tarefa: Armazene os nomes dos pacientes em uma matriz 5x3 e exiba a agenda completa.

agenda = []

dias_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]

for i in range(5):
    linha = []
    for j in range(3):
        paciente = input(f"\nDigite o nome do paciente para {dias_semana[i]} no {j+1}° horário: ")
        linha.append(paciente)
    agenda.append(linha)

print("\n=== Agenda Semanal do Consultório ===")
for i in range(5):
    print(f"\n{dias_semana[i]}:")
    for j in range(3):
        print(f"Horário {j+1}: {agenda[i][j]}")

print("\nMatriz da agenda:", agenda)