entrada = input().split()
quantidade = int(entrada[0])
entrada = list(map(int,entrada[1:]))
entrada.sort()
print(entrada)
var = []

'''for i in range(quantidade):
    i +=1
    var.append(i)
print(entrada)

for i in var:
    if i not in entrada:
        print(i)'''

cont=0
for i in range(quantidade):
    i+=1
    if i!=entrada[cont]:
        print(i)
        break
    cont+=1
    
