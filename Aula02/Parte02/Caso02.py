#2. Calcule a distância total percorrida. 
#3. Mostre a maior e a menor distância. 
#4. Calcule a média das distâncias arredondada para cima (use math.ceil).
import math
def km():
    print("\n===Distâncias em Km===\n")

    km = []

    for i in range(6):
        distancia = float(input(f"Digite a {i+1}° distância percorrida: "))
        km.append(distancia)
        print(f"Distância de {distancia} km, salva com sucesso!")

    soma = sum(km)
    maior = max(km)
    menor = min(km)
    media = sum(km)/len(km)
    m_d_a = math.ceil(media)

    print(f"\nTotal de distãncia percorridas: {soma} km.")
    print(f"A maior distância: {maior} km.\nA menor distância: {menor}km.")
    print(f"A média da distância: {media} km.")
    print(f"A média das distâncias arredondadas: {m_d_a} km.\n")

km()