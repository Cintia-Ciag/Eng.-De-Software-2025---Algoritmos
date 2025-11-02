# 2.Capturando exceções múltiplas: Crie um programa que peça ao usuário o nome 
# de uma cor e mostre seu valor em RGB de acordo com um dicionário pré-definido. 
# O programa deve tratar exceções caso o nome da cor não exista no dicionário.
# cores = {'vermelho': (255, 0, 0), 'verde': (0, 255, 0), 'azul': (0, 0, 255)}

cores = {'vermelho': (255, 0, 0), 'verde': (0, 255, 0), 'azul': (0, 0, 255)}

try:
    print("\n***Consulta de Cores***\n")
    cor = input("Digite uma cor: ")

    rgb = cores[cor]

except KeyError:
    print("\nCor não encontrada!")

except Exception as erro:
    print(f"Erro: {erro}")

else:
    print(f"A cor '{cor}' em RGB é: {rgb}")
    print(f"RGB: R={rgb[0]}, G={rgb[1]}, B={rgb[2]}")

finally:
    print("Fim da consulta")
    
