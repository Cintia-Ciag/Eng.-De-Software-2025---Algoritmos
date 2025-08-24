#Crie uma função que verifique se um número é primo.

def num_primo(num):
    if num <= 1:
        return False
for i in range (2,int(num ** 0.5)+1):
   if num % i == 0:
       return False
   else:
       return True
    
num =int(input("Digite um número: "))
if num_primo(num):
   print(f"{num} é primo.")
else:
   print(f"{num} não é primo.")

