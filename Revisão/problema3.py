# Problema 3 – Loja de Música Online com Estatísticas 
# Uma loja virtual armazena músicas em uma lista de dicionários, cada música com: 
# titulo, artista, downloads, avaliacoes (lista de notas de 1 a 5). 
# Tarefas: 
# 1. Crie uma função que calcule a nota média de avaliação de cada música. 
# 2. Crie uma função que mostre qual artista tem o maior número total de downloads 
# somando todas as suas músicas. 
# 3. Monte um ranking das músicas mais bem avaliadas (ordem decrescente da média das 
# notas).

musicas = [
    {
        "titulo": "Back in Black",
        "artista": "AC/DC",
        "downloads": 6800,
        "avaliacoes": [5, 4, 5, 5, 4, 5]
    },
    {
        "titulo": "Stairway to Heaven",
        "artista": "Led Zeppelin",
        "downloads": 8900,
        "avaliacoes": [5, 5, 4, 5, 5, 5]
    },
    {
        "titulo": "Enter Sandaman",
        "artista": "Metallica",
        "downloads": 8100,
        "avaliacoes": [5, 5, 5, 4, 4, 5, 5]
    },
]

# 1. Crie uma função que calcule a nota média de avaliação de cada música. 

def nota_media_musica():
    print("1. Nota média de cada música:")
    for musica in musicas:
        avaliacoes = musica["avaliacoes"]
        if not avaliacoes:
            media = 0
        else:
            soma = 0
            for nota in avaliacoes:
                soma = soma + nota
            media = soma / len(avaliacoes)
        print(f"{musica['titulo']}: {media:.1f}")

nota_media_musica()

# 2. Crie uma função que mostre qual artista tem o maior número total de downloads 
# somando todas as suas músicas. 

def artista_mais_downloads():
    downloads_por_artista = {}
    for musica in musicas:
        artista = musica["artista"]
        downloads = musica["downloads"]
        if artista in downloads_por_artista:
            downloads_por_artista[artista] = downloads_por_artista[artista] + downloads
        else:
            downloads_por_artista[artista] = downloads
    
    maior_downloads = 0
    artista_mais = ""
    for artista, total in downloads_por_artista.items():
        if total > maior_downloads:
            maior_downloads = total
            artista_mais = artista
    
    return artista_mais, maior_downloads
artista, total = artista_mais_downloads()
print(f"\n2. Artista com mais downloads: {artista} ({total} downloads)")

# 3. Monte um ranking das músicas mais bem avaliadas (ordem decrescente da média das 
# notas).

def ranking_musicas():
    musicas_com_media = []
    for musica in musicas:
        avaliacoes = musica["avaliacoes"]
        if not avaliacoes:
            media = 0
        else:
            soma = 0
            for nota in avaliacoes:
                soma = soma + nota
            media = soma / len(avaliacoes)
        musicas_com_media.append((musica["titulo"], media))
    
    ranking = []
    while musicas_com_media:
        maior_media = -1
        musica_maior = ""
        indice_remover = -1
        for i, (titulo, media) in enumerate(musicas_com_media):
            if media > maior_media:
                maior_media = media
                musica_maior = titulo
                indice_remover = i
        ranking.append((musica_maior, maior_media))
        musicas_com_media.pop(indice_remover)
        return ranking

print("\n3. Ranking das músicas mais bem avaliadas:")
ranking = ranking_musicas()
for pos, (titulo, media) in enumerate(ranking, 1):
    print(f"{pos}. {titulo}: {media:.1f}")
    