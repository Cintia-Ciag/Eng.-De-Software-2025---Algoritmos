#Caso5: Controle de Participação em um Evento 
#Os organizadores de um evento registraram os nomes dos participantes de cada atividade em 
#listas separadas. 
#• Exemplo: 
#o Palestra: ["Ana", "Carlos", "Marina"] 
#o Workshop: ["Carlos", "João", "Ana"] 
#o Mesa-redonda: ["Marina", "João", "Paula"] 
#Eles precisam: 
#1. Saber quem participou de todas as atividades. 
#2. Saber quem participou de apenas uma atividade. 
#3. Gerar uma lista com todos os nomes únicos dos participantes. 
#4. Contar quantos participantes distintos houve no evento.

print("\n==Controle de Participação==\n")

Palestra = ["Ana", "Carlos", "Marina", "Cintia"] 
Workshop =["Carlos", "Cintia",  "João", "Ana",] 
Mesa_redonda = ["Marina", "João", "Cintia", "Paula"] 

todos = set(Palestra) & set(Workshop) & set(Mesa_redonda)
print("1. Quem participou de todas as atividades: ",todos)

uma = []
for pessoa in set(Palestra + Workshop + Mesa_redonda):
    total = (pessoa in Palestra) + (pessoa in Workshop) + (pessoa in Mesa_redonda)
    if total == 1:
        uma.append(pessoa)
        print("2. Quem participou de apenas uma atividade: ",uma)

todos_nomes = set(Palestra + Workshop + Mesa_redonda)
print("3. Lista de todos os participantes:", todos_nomes)

print("4. Quantidade de participantes distintos que tiveram no evento: ", len(todos_nomes))