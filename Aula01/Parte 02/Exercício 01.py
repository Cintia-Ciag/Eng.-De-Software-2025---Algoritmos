# Cálculo de complexidade simples

n = int(input("Digite um número: "))

soma = 0
operacoes = 0

for i in range (1,n + 1):
    soma += i
    operacoes += 1
   
formula = n *(n + 1)//2

print ("\n ***Resultados***")
print ("Soma calculada com laço: ", soma)
print ("Número de operações de soma realizadas: ", operacoes)
print ("Soma pela fórmula matemática:", formula)
