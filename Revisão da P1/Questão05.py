# 5. Você deve criar um programa em Python que utilize um dicionário para 
# armazenar as informações de funcionários de uma empresa. O programa 
# deve ser capaz de fazer o seguinte: 
# (A) Perguntar o nome, o salário e o cargo de cada funcionário. 
# (B) Armazenar essas informações em um dicionário, onde a chave 
# será o nome do funcionário e o valor será outro dicionário com 
# as informações de salário e cargo. 
# (C) O programa deve permitir ao usuário consultar o salário e o 
# cargo de um funcionário informando seu nome. 
# (D) O programa também deve permitir que o usuário liste todos os 
# funcionários cadastrados, mostrando seu nome, cargo e 
# salário.

informacoes = {}

while True:
    print("\n===MENU===")
    print("1. Adicionar funcionário")
    print("2. Consultar funcionário")
    print("3. Listar todos os funcionários")
    print("4. Sair")
    
    opcao = input("\nDigite sua opção: ")

    if opcao == "1":
        nome = input("\nDigite seu nome: ")
        salario = input("Digite seu Salário: ")
        cargo = input("Digite seu cargo: ")
        informacoes.update({nome:{"Salário":salario, "cargo":cargo}})
        print(f"Funcionário {nome} adicionado com sucesso!")

    elif opcao == "2":
        consultar_informacoes = input("Digite o nome do funcionário que deseja consultar: ")
        if consultar_informacoes in informacoes:
            dados = informacoes[consultar_informacoes]
            print(f"Nome: {consultar_informacoes}")
            print(f"Cargo: {dados["cargo"]}")
            print(f"Salário: {dados["Salário"]}")
        else:
            print("Funcionário não encontrado!")
    
    elif opcao == "3":
        if not informacoes:
            print("Nenhum funcionário encontrado!")
        else:
            print("\nLista de Funcionários")
            for nome, dados in informacoes.items():
                print(f"Nome: {nome}, Cargo:{dados["cargo"]}, Salário: {dados["Salário"]}")

    elif opcao == "4":
        print("Saíndo do Programa!")
        break

    else:
        print("Opção Inválida! Tente Novamente.")