# Estatísticas de notas

entrada = input("\nDigite as notas: ")

notas =[float(n) for n in entrada.split()]

media = sum(notas) / len(notas)

maior = max(notas)
menor = min(notas)

acima_media = [n for n in notas if n > media]

percentual = (len(acima_media)/len(notas))*100

print("\n---Estatísticas da Turma---")
print(f"\n Média da turma: {media}\n Maior nota: {maior}\n Menor nota: {menor}\n Percentual de alunos acima da média: {percentual} ")
