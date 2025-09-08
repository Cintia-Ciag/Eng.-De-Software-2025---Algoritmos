# validação de login

senha_correta = "senha123"

tentativas = 0

limite = 3

while tentativas < limite:
    senha_digitada = input("\nDigite a sua senha: ")
   
    if senha_digitada == senha_correta:
       print("Bem Vindo!")
       break

    else:
        tentativas += 1
        restante = limite - tentativas
        
    
    if restante > 0:
        print ("Senha Incorreta!")
        print (f"Você tem mais {restante} tentativas.")
    else:
        print ("Acesso Negado!")
        print ("Tentativas Esgotadas.")
