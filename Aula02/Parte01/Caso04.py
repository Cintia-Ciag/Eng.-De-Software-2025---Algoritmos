#Estudo de Caso 4 - Controle de Vendas em uma Loja de Eletrônicos 
#Contexto do Problema 
#Imagine que você trabalha em uma loja de eletrônicos que precisa organizar melhor o registro 
#diário de vendas. Até então, os vendedores anotavam em papel ou planilhas, mas o dono pediu 
#para criar um programa simples em Python para armazenar, analisar e gerar pequenos 
#relatórios sobre as vendas do dia. 
#O sistema precisa: 
#1. Guardar os produtos vendidos (nome e preço). 
#2. Mostrar o valor total arrecadado. 
#3. Identificar o produto mais caro e o mais barato do dia. 
#4. Permitir consultar se um produto específico foi vendido.

vendas = []

def registrar():
    
    print("\nControle de Vendas da Loja de Eletrônicos\n")
    iten=input("Qual o nome do produto? ")
    valor=float(input("Qual o preço do produto? R$ "))
    vendas.append({"nome":iten, "preco":valor})
    print(f"\nProduto {iten} registrado com sucesso!\n")
            
def total_arrecadado():
    if not vendas:
        print("\nNenhuma venda registrada!")
    total = sum(v["preco"]for v in vendas)
    print(f"Valor total arrecadado: R$ {total:.2f}\n")

def caro_barato():
    if not vendas :
        print("Nenhuma venda registrada!\n")
        return
    caro =max(vendas, key=lambda x: x["preco"])
    barato=min(vendas, key=lambda x: x["preco"])
    print(f"Produto mais caro: {caro['nome']} (R$ {caro['preco']:.2f})\n")
    print(f"Produto mais barato: {barato['nome']} (R$ {barato['preco']:.2f})\n")

def consultar():
    if not vendas:
        print("Nenhuma venda registrada!\n")
        return
    encontrar = input("Digite o nome do produto para consultar: ").strip()
    encontrado = [v for v in vendas if v["nome"].lower() == encontrar.lower()]
    if encontrado:
        print(f"O produto {encontrar} foi vendido {len(encontrar)} vez(es).\n")
    else:
        print(f"O produto {encontrar} não foi vendido hoje.\n")

def menu():
    while True:
        print("\n=== CONTROLE DE VENDAS ===\n")
        print("1.Registrar venda.\n2.Mostrar total arrecadado\n3.Mostrar o produto mais caro e mais barato\n" \
        "4.Consultar vendas\n5.Sair\n")

        opcao = input("Escolha uma opção: \n")

        if opcao == "1":
            registrar()
        elif opcao == "2":
            total_arrecadado()
        elif opcao == "3":
            caro_barato()
        elif opcao == "4":
            consultar()
        elif opcao ==  "5":
            print("Saindo do Sistema...")
            break
        else:
            print("Opção inválida!\n")
menu()