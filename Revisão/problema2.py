# Problema 2 – Academia e Desempenho dos Atletas 
# A academia guarda os atletas em uma lista de dicionários, cada um com: 
# nome, idade, modalidades (lista de esportes), treinos (dicionário com o nome do esporte como 
# chave e a quantidade de treinos realizados como valor). 
# Tarefas: 
# 1. Crie uma função que calcule a média de idade dos atletas que praticam um esporte 
# específico. 
# 2. Crie uma função que, dado um atleta, informe qual esporte ele mais treinou. 
# 3. Monte uma lista com os atletas que praticam mais de 2 modalidades e exiba seus 
# nomes.

atletas = [
    {
        "nome":"Lucas",
        "idade":20,
        "modalidade":["Natação","Corrida"],
        "treinos":{"Natação":12, "Corrida":8},
    },
    {
        "nome":"Mariana",
        "idade":25,
        "modalidade":["Musculção","Yoga", "Pilates"],
        "treinos":{"Musculação":15, "Yoga":10, "Pilates":5},
    },
    {
        "nome":"Joâo",
        "idade":22,
        "modalidade":["Corrida","Ciclismo"],
        "treinos":{"Corrida":20, "Ciclismo":18},
    },
]

# 1. Crie uma função que calcule a média de idade dos atletas que praticam um esporte 
# específico. 

def media_idade_esporte(esporte):
    soma_idades = 0
    contador = 0
    for atleta in atletas:
        if esporte in atleta["modalidade"]:
            soma_idades = soma_idades + atleta["idade"]
            contador = contador + 1
    if contador == 0:
        return 0
    return soma_idades / contador

print("1. Média de idade dos atletas por esporte:")
print(f"Natação: {media_idade_esporte('Natação'):.1f} anos")
print(f"Corrida: {media_idade_esporte('Corrida'):.1f} anos")
print(f"Musculação: {media_idade_esporte('Musculação'):.1f} anos")

# 2. Crie uma função que, dado um atleta, informe qual esporte ele mais treinou. 

def esporte_mais_treinado(nome_atleta):
    for atleta in atletas:
        if atleta["nome"] == nome_atleta:
            treinos = atleta["treinos"]
            maior_treinos = 0
            esporte_mais = ""
            for esporte, quantidade in treinos.items():
                if quantidade > maior_treinos:
                    maior_treinos = quantidade
                    esporte_mais = esporte
            return esporte_mais
    return

print("\n2. Esporte mais treinado por atleta:")
print(f"Lucas: {esporte_mais_treinado('Lucas')}")
print(f"Mariana: {esporte_mais_treinado('Mariana')}")
print(f"João: {esporte_mais_treinado('João')}")

# 3. Monte uma lista com os atletas que praticam mais de 2 modalidades e exiba seus 
# nomes.

atletas_mais_de_dois = []
for atleta in atletas:
    if len(atleta["modalidade"]) > 2:
        atletas_mais_de_dois.append(atleta["nome"])

print("\n3. Atletas que praticam mais de 2 modalidades:")
if atletas_mais_de_dois:
    for i, nome in enumerate(atletas_mais_de_dois, 1):
        print(f"{i}. {nome}")
else:
    print("Nenhum atleta pratica mais de 2 modalidades.")
