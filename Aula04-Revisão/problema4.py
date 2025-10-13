# Problema 4 – Ranking de Filmes 
# Você recebeu uma lista de filmes (cada filme é um dicionário) com os campos: 
# • titulo → nome do filme 
# • diretor → nome do diretor 
# • bilheteria → valor em milhões de dólares 
# • avaliacoes → lista de notas de 1 a 10 
# Tarefas: 
# 1. Top 3 maiores bilheterias 
# o Crie uma função top_bilheteria(filmes) que retorne os 3 filmes com maior 
# bilheteria. 
# 2. Top 3 melhores avaliados 
# o Crie uma função top_avaliacao(filmes) que calcule a média das avaliações de 
# cada filme e retorne os 3 melhores. 
# 3. Bilheteria por diretor 
# o Crie uma função bilheteria_por_diretor(filmes) que retorne um dicionário onde a 
# chave é o diretor e o valor é o total de bilheteria de todos os seus filmes. 
# 4. Campeão absoluto 
# o Crie uma função campeao(filmes) que mostre qual filme é a melhor combinação 
# de bilheteria alta e avaliação média alta. 

filmes = [
    {
        "titulo": "Inception",
        "diretor": "Christopher Nolan",
        "bilheteria": 830,
        "avaliacoes": [9, 10, 8, 9, 10]
    },
    {
        "titulo": "Avengers: Endgame",
        "diretor": "Anthony Russo",
        "bilheteria": 2797,
        "avaliacoes": [9, 9, 10, 10, 9]
    },
    {
        "titulo": "The Dark Knight",
        "diretor": "Chrstopher Nolan",
        "bilheteria": 1005,
        "avaliacoes": [10, 10, 9, 10, 10]
    },
    {
        "titulo": "Jurassic Park",
        "diretor": "Steven Spielberg",
        "bilheteria": 1029,
        "avaliacoes": [8, 9, 9, 8, 9]
    }
]

#1. Top 3 maiores bilheterias 
# o Crie uma função top_bilheteria(filmes) que retorne os 3 filmes com maior 
# bilheteria. 

def top_bilheteria(filmes):
    ranking = []
    filmes_copia = filmes.copy()
    while len(ranking) < 3 and filmes_copia:
        maior_bilheteria = -1
        filme_maior = None
        indice_remover = -1
        for i, filme in enumerate(filmes_copia):
            if filme["bilheteria"] > maior_bilheteria:
                maior_bilheteria = filme["bilheteria"]
                filme_maior = filme
                indice_remover = i
        ranking.append((filme_maior["titulo"], filme_maior["bilheteria"]))
        filmes_copia.pop(indice_remover)
    return ranking

print("1. Top 3 maiores bilheterias:")
ranking = top_bilheteria(filmes)
for pos, (titulo, bilheteria) in enumerate(ranking, 1):
    print(f"{pos}. {titulo}: {bilheteria} milhões")

# Tarefa 2: Top 3 melhores avaliados
# o Crie uma função top_avaliacao(filmes) que calcule a média das avaliações de 
# cada filme e retorne os 3 melhores.

def top_avaliacao(filmes):
    filmes_com_media = []
    for filme in filmes:
        avaliacoes = filme["avaliacoes"]
        if not avaliacoes:
            media = 0
        else:
            soma = 0
            for nota in avaliacoes:
                soma = soma + nota
            media = soma / len(avaliacoes)
        filmes_com_media.append((filme["titulo"], media))
    
    ranking = []
    while len(ranking) < 3 and filmes_com_media:
        maior_media = -1
        filme_maior = ""
        indice_remover = -1
        for i, (titulo, media) in enumerate(filmes_com_media):
            if media > maior_media:
                maior_media = media
                filme_maior = titulo
                indice_remover = i
        ranking.append((filme_maior, maior_media))
        filmes_com_media.pop(indice_remover)
    
    return ranking

print("\n2. Top 3 melhores avaliados:")
ranking = top_avaliacao(filmes)
for pos, (titulo, media) in enumerate(ranking, 1):
    print(f"{pos}. {titulo}: {media:.1f}")

# Tarefa 3: Bilheteria por diretor
# o Crie uma função bilheteria_por_diretor(filmes) que retorne um dicionário onde a 
# chave é o diretor e o valor é o total de bilheteria de todos os seus filmes. 

def bilheteria_por_diretor(filmes):
    bilheteria_diretor = {}
    for filme in filmes:
        diretor = filme["diretor"]
        bilheteria = filme["bilheteria"]
        if diretor in bilheteria_diretor:
            bilheteria_diretor[diretor] = bilheteria_diretor[diretor] + bilheteria
        else:
            bilheteria_diretor[diretor] = bilheteria
    return bilheteria_diretor

print("\n3. Bilheteria por diretor:")
bilheteria = bilheteria_por_diretor(filmes)
for diretor, total in bilheteria.items():
    print(f"{diretor}: {total} milhões")

# Tarefa 4: Campeão absoluto
# o Crie uma função top_avaliacao(filmes) que calcule a média das avaliações de 
# cada filme e retorne os 3 melhores. 

def campeao(filmes):
    if not filmes:
        return None
    
    max_bilheteria = 0
    max_media = 0
    filmes_com_media = []
    for filme in filmes:
        if filme["bilheteria"] > max_bilheteria:
            max_bilheteria = filme["bilheteria"]
        avaliacoes = filme["avaliacoes"]
        if avaliacoes:
            soma = 0
            for nota in avaliacoes:
                soma = soma + nota
            media = soma / len(avaliacoes)
        else:
            media = 0
        filmes_com_media.append((filme["titulo"], media, filme["bilheteria"]))
        if media > max_media:
            max_media = media
    
    maior_pontuacao = -1
    filme_campeao = ""
    for titulo, media, bilheteria in filmes_com_media:
        if max_bilheteria > 0:
            pontuacao_bilheteria = bilheteria / max_bilheteria
        else:
            pontuacao_bilheteria = 0
        if max_media > 0:
            pontuacao_media = media / max_media
        else:
            pontuacao_media = 0
        pontuacao = pontuacao_bilheteria + pontuacao_media
        if pontuacao > maior_pontuacao:
            maior_pontuacao = pontuacao
            filme_campeao = titulo
    
    return filme_campeao, maior_pontuacao

print("\n4. Campeão absoluto:")
campeao_titulo, campeao_pontuacao = campeao(filmes)
print(f"{campeao_titulo}: pontuação {campeao_pontuacao:.2f}")
