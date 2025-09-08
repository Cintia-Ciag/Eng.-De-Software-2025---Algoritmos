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
    {"Produto":"Açucar", "Quantidade":4, "Preço unitário":12}
    ]


def add():

    while True:
        print("\n===CONTROLE DE ESTOQUE===\n")
        produto =input("\nDeseja adicionar itens na sua lista? Ou digite sair para encerrar.")
        if produto.lower() == "sair":
            break
        qtd = input("\nQuantidade do produto? ")
        if qtd.lower() == "sair":
            break    
        entrada = (input("\nPreço Unitário: "))
        if entrada.lower() == "sair":
            break
        p_u = float(entrada)
        estoque.append({"Produto": produto, "Quantidade": int(qtd), "Preço unitário": p_u})
        print(f"O produto {produto} com quantidade de {qtd} unidades e valor unitário R$ {p_u}, registrado no estoque com sucesso!")


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

    est_baixo = [e["Produto"] for e in estoque if e["Quantidade"] < 5]
                 
    print(f"O valor total em estoque: {vte}\n")
    print(f"O produto de maior valor total: {p_m}\n")
    print(f"Produtos com estoque abaixo de 5 unidades: {est_baixo}")

def buscar():

    nome=input("Digite o nome do produto que deseja buscar:")
    encontrado=None
    for e in estoque:
        if e["Produto"].lower() == nome.lower():
            encontrado = e
            break

    if encontrado:
        print("Produto encontrado!\n")
        print(f"Nome: {encontrado[nome]}\nQuantidade: {encontrado["qtd"]}\nPreço unitário: R$ {encontrado["p_u"]}")
    else:
        print("\nNenhum Produto com esse registro.")

def menu():
    while True:
        print("\n=== CONTROLE DE ESTOQUE DO SUPERMERCADO ===\n")
        print("1.Adicionar ao estoque\n2.Relatório de estoque\n3.Buscar estoque\n")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            add()
        elif opcao == "2":
            relatorio()
        elif opcao == "3":
            buscar()
        else:
            print("Opção inválida!\n")

menu()