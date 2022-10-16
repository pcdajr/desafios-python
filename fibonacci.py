valor = int(input("Digite o valor: "))
a, b = 0, 1
while b < valor:
    print(b)
    a,b = b, a+b
