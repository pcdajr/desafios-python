a = int(input("Quantos cm tem a Aresta 1?:"))
b = int(input("Quantos cm tem a Aresta 2?:"))
c = int(input("Quantos cm tem a Aresta 3?:"))
temp = 0
numeros = a,b,c


#VERSÃO COM O OBJETO LIST
numeros = list(numeros)
kim = max(numeros)
indiceKim = numeros.index(kim)
del numeros[indiceKim]

if  kim <sum(numeros):
    print("É POSSIVEL FORMAR UM TRIÂNGULO COM ESSAS MEDIDAS")
else:
    print("IMPOSSIVEL FORMAR TRIÂNGULO COM ESSAS MEDIDAS")



'''
for i in numeros:
    if int(i) > int(temp):
        maior = i
        temp = maior        
maxi = temp

if int(a) > (int(b) and int(c)):
    soma = int(numeros[1]) + int(numeros[2])

elif int(b) > (int(a) and int(c)):
    soma = int(numeros[0]) + int(numeros[2])
    
elif int(c) > (int(b) and int(a)):    
    soma = int(numeros[1]) + int(numeros[0])

if (int(maxi) < soma):
    print("É POSSIVEL FORMAR UM TRIÂNGULO COM ESSAS MEDIDAS")
else:
    print("IMPOSSIVEL FORMAR TRIÂNGULO COM ESSAS MEDIDAS")
'''

