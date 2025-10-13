# Problema 1 – Restaurante Inteligente
# Um restaurante armazena os pedidos do dia em uma lista de dicionários, onde cada pedido tem:
# cliente, itens (lista de dicionários com prato e preco).
# Tarefas:
# 1. Crie uma função que receba o nome de um cliente e retorne o valor total gasto (somando
# todos os itens pedidos).
# 2. Crie uma função que descubra qual prato foi o mais vendido no dia.
# 3. Mostre um ranking com os 3 clientes que mais gastaram, em ordem decrescente.

pedidos = [
    {
        "cliente": "Ana",
        "itens": [
            {"prato": "Lasanha", "preco": 30},
            {"prato": "Suco de Laranja", "preco": 8}
        ]
    },
    {
        "cliente": "Bruno",
        "itens": [
            {"prato": "Pizza", "preco": 40},
            {"prato": "Refrigerante", "preco": 6},
            {"prato": "sobremesa", "preco": 12}
        ]
    },
    {
        "cliente": "Carla",
        "itens": [
            {"prato": "Pizza", "preco": 40},
            {"prato": "Suco de Laranja", "preco": 8}
        ]
    }
]

# 1. Crie uma função que receba o nome de um cliente e retorne o valor total gasto (somando
# todos os itens pedidos).

def fechamento(cliente, pedidos):
    
    total = 0
    for p in pedidos:
        if p["cliente"] == cliente:
           for item in p["itens"]:
               total += item["preco"]
    return total
    
print("1. Valor total gasto por cada cliente:")
print(f"Ana: R${fechamento('Ana', pedidos):.2f}")
print(f"Bruno: R${fechamento('Bruno', pedidos):.2f}")
print(f"Carla: R${fechamento('Carla', pedidos):.2f}")

# 2. Crie uma função que descubra qual prato foi o mais vendido no dia.

def mais_vendidos(item, pedidos):
    contador = {}  
    for p in pedidos:
        for item in p["itens"]:
            prato = item["prato"]
            if prato in contador:
                contador[prato] += 1  
            else:
                contador[prato] = 1  
    mais_vendido = max(contador, key=contador.get)
    return mais_vendido

print(f"O prato mais vendido: {mais_vendidos("prato", pedidos)}")

# 3. Mostre um ranking com os 3 clientes que mais gastaram, em ordem decrescente.

def clientes_mais_gastaram(total_pedido, pedidos):
    gastos = {} 
    for p in pedidos:
        cliente = p["cliente"]
        total_pedido = sum(item["preco"] for item in p["itens"])
        if cliente in gastos:
            gastos[cliente] += total_pedido  
        else:
            gastos[cliente] = total_pedido  
    ranking = sorted(gastos.items(), key=lambda x: x[1], reverse=True)
    return ranking[:3]

print(f"O ranking com os 3 clientes que mais gastara:{clientes_mais_gastaram("preco", pedidos)}")