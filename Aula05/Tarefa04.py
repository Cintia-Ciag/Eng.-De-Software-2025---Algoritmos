#Nível 1 – Fundamentos
# 3. Maior Número (Busca Linear)
# o Use busca sequencial para encontrar o maior número em uma lista.

def busca_linear(lista, chave):
    for num in lista:
        if num == chave:
            maior = max(lista)
            print(f"O maior número é: {maior}")
    return maior

lista = []
for num in range(5):
    num = int(input("Digite os numeros: "))
    lista.append(num)

resultado = busca_linear(lista, num)

print(resultado)