#1. Receba 10 números inteiros digitados pelo usuário. 
#2. Separe-os em duas listas: pares e ímpares. 
#3. Exiba quantos números pares e ímpares foram digitados.

def par_impar():

    pares =[]
    impares = []

    for i in range(10):

        num = int(input(f"\nDigite o {i+1}° número inteiro: "))
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)

        print("\n***RESULTADO***\n")
        print(f"Números pares digitados: {pares}")
        print(f"Números ímpares digitados: {impares}")
        print(f"Quantidade de números pares: {len(pares)}")
        print(f"Quantidade de números ímpares: {len(impares)}\n")

par_impar()