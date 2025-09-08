# Verificação de CPF (Simplificado)

cpf = input ("\nDigite o seu CPF, só os números: ")

tamanho_valido = len(cpf) == 11

todos_digitos = cpf.isdigit()

if tamanho_valido and todos_digitos:
    print("CPF válido")
 
else:
    print("CPF inválido")
