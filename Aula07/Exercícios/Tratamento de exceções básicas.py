# 1.Tratamento de exceções básicas: Escreva um programa que peça ao usuário dois números e faça a divisão do primeiro pelo segundo.
# Se o usuário inserir um valor inválido ou tentar dividir por zero, o programa deve exibir uma mensagem de erro apropriada.

try:
    n1 = int(input("Digite um número: "))
    n2 = int(input("Digite um número: "))

    resultado = n1 / n2

except ValueError:
    print('Digite um número inteiro e válido!')

except ZeroDivisionError:
    print("Não é possivel dividir por zero.")

else:
    print(f'O resultado eh: {resultado}')

finally:
    print("Operação realizada com sucesso!")