#Desenvolva um programa que leia uma lista de números e mostre a média deles.

entrada = input ("Digite os números separados por espaço: ")

num_str = entrada.split()

numeros=[float(nu)for nu in num_str]

soma = sum(numeros)

quantidade = len(numeros)

media = soma / quantidade

print("A média dos números é: ", media)