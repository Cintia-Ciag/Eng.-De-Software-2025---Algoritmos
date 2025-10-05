# 3. Crie um programa em Python que implemente uma função chamada calcula_imposto_renda.
# A função deve receber um único parâmetro: 
# salário: o valor do salário bruto de um indivíduo. 
# Com base na tabela de alíquotas abaixo, a função deve calcular e 
# retornar o valor do imposto de renda devido: 
# Faixa Salarial (R$)          Alíquota (%)       Dedução (R$)     Faixa Salarial (R$)
# De 2.112,00                  Isento             0                Até 2.112,01 
# De 2.112,01 a 2.826,65       7,50%              158,4            De 2.112,01 a 2.826,66
# De 2.826,66 a 3.751,05       15%                370,4            De 2.826,66 a 3.751,06 
# De 3.751,06 a 4.664,68       22,50%             651,73           De 3.751,06 a 4.664,69 
# Acima de 4.664,68            27,50%             884,96           Acima de 4.664,69 
# Requisitos: 
# • A função deve retornar o valor do imposto de renda a ser pago. 
# • O programa deve solicitar ao usuário o salário bruto, chamar a função e exibir o imposto devido.
# Exemplo:
# Entrada 
# salario = 3500.00
# Saídas
# salário bruto: R$ 3500.00
# Imposto de Renda Devido: R$ 524.60

def calcula_imposto_renda(salario_bruto):

    if salario_bruto < 2112.01:
        deducao = 0.0
        alíquota = 0.0
        imposto = (salario_bruto * alíquota / 100) - deducao
        return imposto

    elif salario_bruto <= 2826.65:
        deducao = 158.4
        alíquota = 7.5
        imposto = (salario_bruto * alíquota / 100) - deducao
        return imposto

    elif salario_bruto <= 3751.06:
        deducao = 370.4
        alíquota = 15
        imposto = (salario_bruto * alíquota / 100) - deducao
        return imposto
    
    elif salario_bruto <= 4664.68:
        deducao = 651.73
        alíquota = 22.5
        imposto = (salario_bruto * alíquota / 100) - deducao
        return imposto
    
    elif salario_bruto > 4664.68:
        deducao = 884.96
        alíquota = 27.5
        imposto = (salario_bruto * alíquota / 100) - deducao
        return imposto
    
salario_bruto = float(input("\nDigite seu salário bruto: "))
    
imposto_de_renda = calcula_imposto_renda(salario_bruto)
virpago = imposto_de_renda 

print(f"\nSalário Bruto: {salario_bruto:.2f}")
print(f"Imposto de Renda Devido: {virpago:.2f}\n")