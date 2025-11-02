# 3.Bloco else e finally: Escreva um programa que solicite um número ao usuário. 
# Se o número for maior que 10, exiba uma mensagem dizendo que o número é válido.
#  Utilize o bloco else para imprimir que o programa foi executado com sucesso, e o bloco finally para imprimir "Programa encerrado".

try:

    num = int(input("\nDigite um número: "))

    if num > 10:
        print("O número é válido!")
    else:
        print("O número inválido!")

except ValueError:
    print("Erro: Digite um número inteiro!")

else:
    print("O programa foi executado com sucesso!")

finally:
    print("Programa encerrado!")