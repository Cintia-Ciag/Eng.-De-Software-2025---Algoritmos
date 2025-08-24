# validação de login

senha_correta = "senha123"

tentativas = 0

while tentativas < 3:
    senha_digitada = input("Digite a sua senha: ")
   
    if senha_digitada == senha_correta:
       print("Bem Vindo!")
       break
    else:
        print ("Senha Incorreta!")
        print ("Você tem mais duas tentativas.")
       
    tentativas += 1
    
    if tentativas == 3:
        print ("Acesso Negado!")
        print ("Tentativas Esgotadas.")
