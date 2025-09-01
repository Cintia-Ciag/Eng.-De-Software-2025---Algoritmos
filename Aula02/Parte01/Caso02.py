#Faça um programa que: 
#1. Permita ao usuário adicionar itens a uma lista de compras. 
#2. Caso o usuário digite "sair", o programa encerra. 
#3. Mostre a lista final de compras organizada em ordem alfabética.
def lista_compras():

    lista=[]
    
    while True:
        print("\n---Lista de Compras---\n")
        itens =input("\nDeseja adicionar itens na sua lista? Ou digite sair para encerrar.")
        if itens.lower() == "sair":
            break
        else:
            lista.append(itens)
            lista.sort()
            print("\nLista final das compras: ")
            for i, produto in enumerate(lista, start=1):
                print(f"{i}, {produto}")

lista_compras()