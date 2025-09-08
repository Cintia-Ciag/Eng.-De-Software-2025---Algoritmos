#Caso1: Controle de Presença em Sala de Aula 
#Uma professora precisa registrar a presença dos alunos durante a semana. 
#• Cada dia da semana terá uma lista com os nomes dos presentes. 
#• No final, ela precisa: 
#1. Saber quais alunos estiveram presentes todos os dias. 
#2. Saber quais alunos faltaram em pelo menos um dia. 
#3. Saber o número total de presenças por aluno.

#Dicionários Python
segunda = []
terca = []
quarta = []
quinta = []
sexta = []
semana = [segunda, terca, quarta, quinta, sexta]

def seg():
    print("===Presenças de Segunda Feira===\n")
    for i in range (5):
        aluno = input(f"Digite o {i+1}° nome do aluno presente: ")
        segunda.append(aluno)
        segunda.sort()
    print("\nAté amanhã, Professor(a)!\n")

def ter():
    print("===Presenças de Terça Feira===\n")
    for i in range (5):
        aluno = input(f"Digite o {i+1}° nome do aluno presente: ")
        terca.append(aluno)
        terca.sort()
    print("\nAté amanhã, Professor(a)!\n")

def qua():
    print("===Presenças de Quarta Feira===\n")
    for i in range(5):
        aluno = input(f"Digite o {i+1}° nome do aluno presente: ")
        quarta.append(aluno)
        quarta.sort()
    print("\nAté amanhã, Professor(a)!\n")

def qui():
    print("===Presenças de Quinta Feira===\n")
    for i in range(5):
        aluno = input(f"Digite o {i+1}° nome do aluno presente: ")
        quinta.append(aluno)
    print("\nAté amanhã, Professor(a)!\n")

def sex():
    print("===Presenças de Sexta Feira===\n")
    for i in range(5):
        aluno = input(f"Digite o {i+1}° nome do aluno presente: ")
        sexta.append(aluno)
        sexta.sort()
    print("\nAté Segunda, Professor(a)!\n")

def relatorio():
    print("===Relatório da Semana===\n")
    p_t_d = set(segunda)
    for dia in semana:
        p_t_d = p_t_d.intersection(dia)

    t_alunos = set(segunda + terca + quarta + quinta + sexta)
    f_a_d = set(segunda)
    for dia in semana:
        f_a_d = t_alunos - p_t_d
   
    t_p = {}
    for aluno in t_alunos:
        t_p[aluno] = 0
        for dia in semana:
            if aluno in dia:
                t_p[aluno] += 1

    print(f"Presentes todos os dias: {p_t_d}\nFaltaram pelo menos um dia: {f_a_d}\nTotal de Presenças: {t_p}")

def menu():
    while True:
        print("\n=== CONTROLE DE PRESENÇAS ===\n")
        print("1.Segunda Feira.\n2.Terça Feira\n3.Quarta Feira\n" \
        "4.Quinta Feira\n5.Sexta Feira\n6.Relatórios\n7.Sair\n")

        opcao = input("Escolha uma opção: \n")

        if opcao == "1":
            seg()
        elif opcao == "2":
            ter()
        elif opcao == "3":
            qua()
        elif opcao == "4":
            qui()
        elif opcao ==  "5":
            sex()
        elif opcao == "6":
            relatorio()
            break
        elif opcao == "7":
            print("Saindo do Sitema...")
            break
        else:
            print("Opção inválida!\n")

menu()