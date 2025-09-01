# Escreva um algoritmo que calcule a tabuada de um número digitado pelo usuário.

print("\n***TABUADA***\n")
Num = int(input("Digite um número: "))
for i in range (0,11):
    resultado = Num * i
    print (f"{Num} X {i} = {resultado}")
