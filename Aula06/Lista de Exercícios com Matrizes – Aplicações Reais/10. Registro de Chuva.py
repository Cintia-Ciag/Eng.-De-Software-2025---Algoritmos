# 10. Registro de Chuva
# Contexto: Uma estação meteorológica registra chuva em 7 dias, para 3 cidades.
# Tarefa: Crie uma matriz 3x7 com os valores de chuva (mm) e determine qual cidade teve mais
# chuva na semana.

chuva = []
cidades = ["Saquarema", "Maricá", "Araruama"]
dias = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sab", "Dom"]

for i in range(3):
    linha = []
    for j in range(7):
        valor = float(input(f"\nDigite a chuva em {cidades[i]} no dia {dias[j]} (em mm): "))
        linha.append(valor)
    chuva.append(linha)

print("\n=*= Total de Chuva por Cidade =*=")
maior_chuva = 0
cidade_vencedora = ""
for i in range(3):
    total_chuva = sum(chuva[i])
    print(f"\nTotal de chuva em {cidades[i]}: {total_chuva:.2f} mm")
    if total_chuva > maior_chuva:
        maior_chuva = total_chuva
        cidade_vencedora = cidades[i]

print(f"\nA cidade com mais chuva foi {cidade_vencedora} com {maior_chuva:.2f} mm!")

print("\nMatriz de chuva:", chuva)