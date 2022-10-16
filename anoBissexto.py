ano = input("Digite ano:")
print("%d Dígitos"%((len(ano))))
if len(ano) != 4:
    print("Ano deve ter 4 dígitos")
    exit 
elif int(ano) % 4 == 0:
    print("É Bissexto")
else:
    print("Não é Bissexto")
