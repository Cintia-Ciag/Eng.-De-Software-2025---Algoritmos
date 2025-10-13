#Nível 1 – Fundamentos
# 2. Contar Ocorrências (Busca Linear)
# Conte quantas vezes um número aparece na lista usando busca sequencial.

lista = [10, 50, 100, 90, 60, 43, 90, 50, 90]

def busca_linear(lista, chave):
    contar_ocorrencias = 0
    for num in lista:
        if num == chave:
            contar_ocorrencias += 1
    print(f"\nO número {num} aparece {contar_ocorrencias}  vezes na lista.")
    return contar_ocorrencias

num =int(input("\nDigite um número: "))
resultado = busca_linear(lista, num)
print(resultado)