#Caso3: Supermercado – Controle de Estoque 
#Um supermercado mantém uma lista de produtos e seus preços. 
#• Cada item será representado como [nome, quantidade, preco_unitario]. 
#• O sistema deve: 
#1. Calcular o valor total em estoque. 
#2. Encontrar o produto de maior valor total (quantidade × preço). 
#3. Gerar uma lista apenas com os nomes dos produtos com estoque abaixo de 5 unidades. 
#4. Permitir buscar um produto pelo nome e retornar seus dados

estoque = [
    {"Produto":"Arroz", "Quantidade":10 , "Preço unitário":26.80},
    {"Produto":"Feijão", "Quantidade":8, "Preço unitário":12.50},
    {"Produto":"Macarrão", "Quantidade":12, "Preço unitário":7.56},
    {"Produto":"Aveia", "Quantidade":5, "Preço unitário":6.0},
    
    ]


def add():

    while True:
        print("\n===CONTROLE DE ESTOQUE===\n")
        produto =input("\nDeseja adicionar itens na sua lista? Ou digite 1 para encerrar.")
        if produto.lower() == "sair":
            break
        qtd = input("\nQuantidade do produto? ")
        if qtd.lower() == "sair":
            break
        p_u = float(input("\nPreço Unitário: "))
        if p_u.lower() == "sair":
            break
        else:
            estoque.append(produto)
            estoque.append(qtd)
            estoque.append(p_u)
            print(f"O produto {produto} com quantidade de {qtd} de valor unitário R$ {p_u}, registrado no estoque com sucesso!")

def relatorio():
        
    vte = 0
    for e in estoque:
        vte += e["Quantidade"] * e["Preço unitário"]

    mv = 0
    p_m = None
    for e in estoque:
        v = e["Quantidade"]* e["Preço unitário"]
        if v > mv:
            mv = v
            p_m = e

        est_baixo = []
        for e in estoque:
            if e["Quantidade"] < 5:
                est_baixo.append(e["produto"])
            else:
                print("Nenhum produto em estoque baixo.")

    print(f"O valor total em estoque: {vte}\n")
    print(f"O produto de maior valor total: {p_m}\n")
    print(f"Produtos com estoque abaixo de 5 unidades: {est_baixo}")

def buscar():

    nome=input("Digite o nome do produto que deseja buscar:")
    encontrado=None
    for e in estoque:
        if e["produto"].lower() == nome.lower():
            encontrado = e
            break
        if encontrado:
            print("Produto encontrado!\n")
            print(f"Nome: {encontrado[nome]}\nQuantidade: {encontrado["qtd"]}\nPreço unitário: R$ {encontrado["p_u"]}")

def menu():
    while True:
        print("\n=== CONTROLE DE ESTOQUE DO SUPERMERCADO ===\n")
        print("1.Adicionar ao estoque\n2.Relatório de estoque\n3.Buscar estoque\n4.Conferir estoque\n5.Sair\n")

        opcao = input("Escolha uma opção: \n")

        if opcao == "1":
            add()
        elif opcao == "2":
            relatorio()
        elif opcao == "3":
            buscar()
        elif opcao == "4":
            print(estoque)
        elif opcao ==  "5":
            print("Saindo do Sistema...\n")
        else:
            print("Opção inválida!\n")

menu()