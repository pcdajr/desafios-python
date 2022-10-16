n1 = int(input("Digite número:"))
n2 = int(input("Digite número:"))
n3 = int(input("Digite número:"))

lista = n1,n2,n3
menor = 0
medio = 0
maior = 0
temp = 0
result = 0
aux = 0

#Achando o maior valor
for i in lista:
    if i > temp:
        temp = i
        maior = temp
    elif i < temp:
        temp = i
        maior = temp
      
#Achando o menor e médio        
if lista[0] == maior:
    if lista[1] > lista[2]:
        menor = lista[2]
        medio = lista[1]
    else:
        menor = lista[1]
        medio = lista[2]
     
elif lista[1] == maior:
    if lista[0] > lista[2]:
        menor = lista[2]
        medio = lista[0]    
    else:
        menor = lista[0]
        medio = lista[2]

elif lista[2] == maior:
    if lista[0] > lista[1]:
        menor = lista[1]
        medio = lista[0]    
    else:
        menor = lista[0]
        medio = lista[1]
       

result = maior,medio,menor   
print("resultado:",result)
