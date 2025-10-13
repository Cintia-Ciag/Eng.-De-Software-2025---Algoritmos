#Nível 1 – Fundamentos
# 4. Menor Número (Busca Linear)
# o Similar ao anterior, mas encontre o menor valor.

def busca_linear(lista, chave):
    for num in lista:
        if num == chave:
            menor = min(lista)
            print(f"O menor número é: {menor}")
    return menor

lista = []

for num in range(5):
    num = int(input("Digite seus números: "))
    lista.append(num)

resulatdo = busca_linear(lista, num)
print(resulatdo)