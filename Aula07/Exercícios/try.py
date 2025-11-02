try: # tentei

    n1 = int(input("Valor 1: "))
    n2 = int(input("Valor 1: "))
    resultado = n1/n2

# Formas de tratar os erros que já sabemos
except ZeroDivisionError: # deu erro
    print("Não é possível divisão por 0. ")

except ValueError:
    print("Digite apenas valores inteiros: ")

else: # acertei
    print(f"O resultado eh: {resultado}")

# Forma de descobrir o erro
# except Exception as erro:  # Classes de erros conhecidos. uma classe de exeções. Esse trata todos os erros
#     print(f'O erro foi de : {erro}')

finally: # finalizar a operação
    print("Operação realizada com sucesso!")



# try, except, finally é usado dependendo do caso: aplicação em banco, é usado pra criar um log um registro falando tudo o que está acontecendo.
# Para tratar banco de dados 
# Para API
# Usar o try no desafio tratativa.