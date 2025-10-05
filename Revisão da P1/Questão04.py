# 4. A empresa TPVFR (Todo Programador Vai Ficar Rico) deseja conceder 
# aumento salarial aos seus programadores. O aumento será calculado 
# conforme o salário atual do programador, de acordo com as seguintes 
# regras:  
# (A).Salários até R$ 2800,00: aumento de 20%. 
# (B).Salários entre R$ 2800,01 e R$ 7000,00: aumento de 15%. 
# (C).Salários entre R$ 7000,01 e R$ 15000,00: aumento de 10%. 
# (D).Salários acima de R$ 15000,00: aumento de 5%. 
# Escreva um programa que recebe o salário de um programador e calcula 
# o salário atualizado com o aumento.

salario = float(input("\nDigite o seu salário: "))

if salario <= 2800.00:
    aumento = salario * (20 / 100)
    salario_atualizado = salario + aumento
    print(f"Seu Salário Atualizado {salario_atualizado}, com aumento de 20%. ")

elif salario <= 7000.00:
    aumento = salario * (15 / 100)
    salario_atualizado = salario + aumento
    print(f"Seu Salário Atualizado {salario_atualizado}, com aumento de 15%. ")

elif salario <= 15000.00:
    aumento = salario * (10 / 100)
    salario_atualizado = salario + aumento
    print(f"Seu Salário Atualizado {salario_atualizado}, com aumento de 10%. ")

elif salario > 15000.00:
    aumento = salario * (5 / 100)
    salario_atualizado = salario + aumento
    print(f"Seu Salário Atualizado {salario_atualizado:.2f}, com aumento de 5%. ")

else:
    print("ERRO: Tente novamente...")