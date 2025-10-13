# Nível 2 – Aplicações Práticas
# 10. Localizar Intervalo de Índices
# • Encontre o intervalo (início e fim) de um número que aparece mais de uma vez usando
# busca binária (ex: [1,2,2,2,3,4] > número 2 > índices 1 a 3).

def busca_binaria(lista, chave):
    pos_inicio = 0
    pos_fim = len(lista) -1
    inicio = -1
    while pos_inicio <= pos_fim:
        pos_meio = (pos_inicio + pos_fim) // 2
        if lista[pos_meio] == chave:
             inicio = pos_meio
             pos_fim = pos_meio -1
        elif lista[pos_meio] > chave:
            pos_inicio = pos_meio + 1
        else:
            pos_inicio = pos_meio + 1
    if inicio == -1:
        return (-1,-1)
    
    pos_inicio = 0
    pos_fim = len(lista) - 1
    fim = -1
    while pos_inicio <= pos_fim:
        pos_meio = (pos_inicio + pos_fim) // 2
        if lista[pos_meio] == chave:
            fim = pos_meio
            pos_inicio = pos_meio + 1  # Continue direita
        elif lista[pos_meio] < chave:
            pos_inicio = pos_meio + 1
        else:
            pos_fim = pos_meio - 1
    return (inicio, fim)
    
    
lista = [1,2,2,2,3,4]
chave = 2
resultado = busca_binaria(lista, chave)
print(f" o intervalo de {chave} é {resultado}")