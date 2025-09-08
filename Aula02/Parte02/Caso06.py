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

print("\n ***Sistema de Biblioteca*** \n")
 
sistema=[
    ["Dom Casmurro", "Ana", 5],
    ["1984", "Carlos", 12],
    ["O Hobbit", "Marina", 3]
         ]

emp_mais_7 = [livro for livro in sistema if livro[2] > 7]
print("1) Livros emprestados há mais de 7 dias:")
for l in emp_mais_7:
    print(f" - {l[0]} (usuário: {l[1]}, dias: {l[2]})")
if not emp_mais_7:
    print(" - Nenhum")

if sistema:
    max_dias = max(l[2] for l in sistema)
    livros_mais_tempo = [l for l in sistema if l[2] == max_dias]
else:
    livros_mais_tempo = []

print("\n2) Livro(s) emprestado(s) há mais tempo:")
for l in livros_mais_tempo:
    print(f" - {l[0]} (usuário: {l[1]}, dias: {l[2]})")

usuarios = list(dict.fromkeys(l[1] for l in sistema))
print("\n3) Usuários com livros emprestados:")
print(usuarios)

media = sum(l[2] for l in sistema) / len(sistema) if sistema else 0
print(f"\n4) Média de dias de empréstimo: {media:.2f}")