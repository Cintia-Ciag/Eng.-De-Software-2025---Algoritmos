# Considere as atividades da Lista 2(aula anterior)

# Caso4: Análise de Vendas Mensais
# Caso6: Sistema de Biblioteca
# Implemente os códigos usando Dicionários.

#Caso6: Sistema de Biblioteca 
#Uma biblioteca mantém uma lista de livros emprestados, onde cada item é representado por 
#[titulo, usuario, dias_emprestado]. 
#Exemplo: 
#[ 
#] 
#["Dom Casmurro", "Ana", 5], 
#["1984", "Carlos", 12], 
#["O Hobbit", "Marina", 3] 
#O sistema precisa: 
#1. Listar apenas os livros que estão emprestados há mais de 7 dias. 
#2. Encontrar o livro emprestado há mais tempo. 
#3. Gerar uma lista apenas com os nomes dos usuários que têm livros emprestados. 
#4. Calcular a média de dias de empréstimo.

emprestimo = {

    "livro1":{
        "titulo": "Dom Casmurro",
        "usuario": "Ana",
        "dias_emprestado": 5
              },
    "livro2":{
        "titulo":"1984",
        "usuario": "Carlos",
        "dias_emprestado": 12
              },
    "livro3":{
        "titulo":"O Hobbit",
        "usuario": "Marina",
        "dias_emprestado": 3
              }
}
for chave, valor in emprestimo.items():
    print(chave, valor)

empmais7dias = [e for e in emprestimo.values() if e["dias_emprestado"] > 7 ] 
print("1) Livros emprestados há mais de 7 dias:")
for l in empmais7dias:
    print(f" - {l['titulo']} (usuário: {l['usuario']}, dias: {l['dias_emprestado']})")

if emprestimo:
    maisdia = max(e["dias_emprestado"] for e in emprestimo.values())
    maistempo = [e for e in emprestimo.values() if e["dias_emprestado"] == maisdia]
else:
    maisdia= 0
    maistempo = []
    print("\n2) Livro(s) emprestado(s) há mais tempo:")
for l in maistempo:
    print(f" - {l['titulo']} (usuário: {l['usuario']}, dias: {l['dias_emprestado']})")

usuarios = list(dict.fromkeys(e["usuario"] for e in emprestimo.values()))
print("\n3) Usuários com livros emprestados (únicos, ordem):")
print(usuarios)

media_dias = sum(e["dias_emprestado"] for e in emprestimo.values()) / len(emprestimo) if emprestimo else 0
print(f"\n4) Média de dias de empréstimo: {media_dias:.2f}")

