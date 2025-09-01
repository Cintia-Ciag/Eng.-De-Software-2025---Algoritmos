#Estudo de Caso 1 – Temperaturas da Semana 
#Enunciado: 
#Crie um programa que: 
#1. Receba as temperaturas de 7 dias e armazene em uma lista. 
#2. Mostre a média das temperaturas da semana. 
#3. Informe o dia mais quente e o dia mais frio. 
#4. Mostre quantos dias ficaram acima da média. 

print("\n***TEMPERATURAS***\n")
temp=input("Digite as temperaturas da semana: ")

tem=[float(t) for t in temp.split()]

media= sum(tem)/len(tem)

maior= max(tem)
menor= min(tem)

acima_media=[t for t in tem if t > media]

percentual= (len(acima_media)/len(tem))*7

print("\n ---TEMPERATURAS DA SEMANA---\n")
print(f"\n A média da Temperatura da semana é: {media}")
print(f"\n A maxima da Temperatura foi: {maior}")
print(f"\n A minima da Temperatura foi: {menor} ")
print(f"\n A Temperatura acima da média foi: {acima_media}")
print(f"\n Quantos dias ficaram acima da média: {percentual}")
