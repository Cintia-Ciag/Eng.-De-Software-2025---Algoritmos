# Estudo de Caso : Cadastro de Produtos
# Um supermercado deseja armazenar informações sobre seus produtos. Cada produto deve
# conter: nome, preço e quantidade em estoque. Utilize um dicionário para representar e
# manipular essas informações.
# Exemplo:
# produto = {"nome": "Arroz", "preco": 25.90, "estoque": 100}
# print(f"O produto {produto["nome"]} custa R${produto["preco"]}")

print("Registro de Produtos")

produto = {
    "produto1":{
        "nome": "Arroz", 
        "preco": 25.90, 
        "estoque": 100,
    },
    "produto2":{
        "nome":"Feijão",
        "preco":12.50,
        "estoque":50,
    },
    "produto3":{
        "nome":"Macarrão",
        "preco":7.50,
        "estoque":80,
    }
}
print("\nLista de produtos:")
for chave, valor in produto.items():
    print(f"{chave}: {valor['nome']} - R${valor['preco']:.2f} - Estoque: {valor['estoque']}")

print(f"\nO {produto['produto1']['nome']} custa R${produto['produto1']['preco']:.2f}")

produto["produto2"]["estoque"] += 20  
print(f"\nNovo estoque de {produto['produto2']['nome']}: {produto['produto2']['estoque']} unidades")

produto["produto4"] = {
    "nome": "Açúcar",
    "preco": 6.40,
    "estoque": 70
}
print("\nLista de produtos atualizada:")
for chave, valor in produto.items():
    print(f"{chave}: {valor['nome']} - R${valor['preco']:.2f} - Estoque: {valor['estoque']}")