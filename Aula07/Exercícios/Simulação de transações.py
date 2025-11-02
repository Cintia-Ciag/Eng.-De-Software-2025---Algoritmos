# 5.Simulação de transações: Crie um programa que simule uma transferência bancária. 
# Peça ao usuário o saldo da conta e o valor da transferência. Caso o saldo seja insuficiente, 
# levante uma exceção do tipo ValueError com a mensagem "Saldo insuficiente". 
# Trate a exceção adequadamente e informe o usuário.

try:
    saldo = float(input("Digite o saldo da sua conta: "))
    valor = float(input("Digite o valor da transferência: "))
    
    if saldo < valor: raise ValueError

except ValueError:
    print(f"Saldo insuficiente!")

else:
    resultado = saldo - valor
    print(f"Transferência efetuada com sucesso!\nSaldo em Conta: R$ {resultado}")
    
finally:
    print("Operação Bem Sucedida!")