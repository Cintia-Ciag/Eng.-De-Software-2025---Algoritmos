# Nível 3 – Desafios
# 11. Busca em Lista de Dicionários
# Dada uma lista de dicionários representando pessoas ({"nome": "Ana", "idade":
# 25}), implemente uma busca linear para encontrar a pessoa com nome "João".

pessoas = [  
    {"nome": "Ana", "idade": 25},
    {"nome": "João", "idade": 46},
    {"nome": "Maria", "idade": 40}
]

def busca_linear(pessoas):
    encontrado = None
    for pessoa in pessoas:  
        if pessoa["nome"] == nome_procurar:  
             encontrado = pessoa  
             break
        if encontrado:
            print(f"Encontrado: {encontrado}")
        else:
             print("Não encontrado")
    return encontrado

nome_procurar = "João"

resultado = busca_linear(pessoas)
print(resultado)