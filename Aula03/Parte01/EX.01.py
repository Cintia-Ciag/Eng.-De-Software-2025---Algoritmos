# 1. Crie um dicionário chamado aluno com as chaves "nome", "idade" e "curso".
# Em seguida, exiba apenas o nome do aluno.
# 2. Adicione uma nova chave "nota" com valor 9.5 ao dicionário aluno.
# Depois, remova a chave "idade".

Aluno={

    "Nome":"Cintia",
    "Idade":"35",
    "Curso":"Inglês"
}

print(Aluno.get("Nome"))
Aluno.update({"Notas":9.5})
print(Aluno)
Aluno.pop("Idade")
print(Aluno)