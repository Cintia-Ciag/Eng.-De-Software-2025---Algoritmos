# 2. Escreva um programa em Python que contenha uma função chamada 
# calcula_bonificacao.  
# (A). 
# Essa função deve receber dois parâmetros:  
# i. taxa_bonus: A porcentagem de bonificação de produção 
# concedida ao funcionário.  
# ii. 
# salario_base: O salário do funcionário antes da bonificação. 
# A função deve calcular e retornar o novo salário do funcionário, já 
# incluindo a bonificação. No programa principal, solicite ao usuário que 
# informe o salário base e a taxa de bonificação, chame a função e exiba o 
# salário final, a bonificação concedida e o salário base informado. 

taxa_bonus = float(input("Informe a taxa de bonificação (%): "))
salario_base = float(input("Informe seu salário: "))

def calcula_bonificacao(taxa_bonus, salario_base):
    bonificacao = salario_base * taxa_bonus / 100
    salario_final = salario_base + bonificacao
    return salario_final

salario_final = calcula_bonificacao(taxa_bonus, salario_base)
bonificacao_concedida = salario_final - salario_base

print(f"Salário Final: {salario_final:.2f}")
print(f"Bonificação Concedida: {bonificacao_concedida:.2f}")
print(f"Salário Base: {salario_base:.2f}")