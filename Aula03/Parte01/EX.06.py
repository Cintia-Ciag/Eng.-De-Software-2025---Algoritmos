# 6. b. Crie um dicionário de notas de 3 alunos (nome como chave, nota como
# valor).
# c. Acesse a nota de um dos alunos e exiba.
# d. Remova um aluno do dicionário de notas.

Notas = {

    "aluno1":{
        "Nome":"Cintia",
        "Nota":9.9
    },
    "aluno2":{
        "Nome":"Carlos",
        "Nota":9.5
    },
    "aluno3":{
        "Nome":"Gabriel",
        "Nota":9.8
    }

}

print(Notas.get("aluno1"))
del Notas["aluno2"]
print(Notas)