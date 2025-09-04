# 3. Dado o dicionário abaixo, escreva um código que exiba cada produto e seu preço:
# produtos = {"Arroz": 15.90, "Feijão": 9.50, "Macarrão": 4.20}

produtos = {"Arroz": 15.90, "Feijão": 9.50, "Macarrão": 4.20}
for chave, valor in produtos.items():
    print(chave, valor)