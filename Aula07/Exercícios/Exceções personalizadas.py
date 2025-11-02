# 4.Exceções personalizadas: Escreva uma função que verifica se uma senha possui no mínimo 8 caracteres e pelo menos um número.
# Se a senha não atender aos requisitos, levante uma exceção com uma mensagem personalizada. 
# Trate a exceção e mostre a mensagem ao usuário.

class senhainvalidaerror(Exception):
    pass

def verificar():
    try:
        senha_digitada = input("Digite a Senha: ").strip() #Pede a senha e remove espaços

        if len(senha_digitada) < 8:
            raise senhainvalidaerror("A senha deve ter no mínimo 8 caracteres.")
        
        if not any(caractere.isdigit() for caractere in senha_digitada):
            raise senhainvalidaerror("A senha deve conter pelo menos um número.")
        

        if senha_digitada == "admin123": 
            raise senhainvalidaerror("Senha válida! Acesso permitido.")
        else:
            raise senhainvalidaerror(f"Senha Errada!{senha_digitada}")

    except senhainvalidaerror as erro:
        print(f"Erro: {erro}")

    finally:
        print("Programa encerrado!")

verificar()