import sys
entrada = list(map(int,input().split(" ")))
tamanhoM = entrada[0]
entrada.remove(tamanhoM)

inicio_linha = 0
final_linha = tamanhoM
passo_dp = 0
passo_ds = tamanhoM -1

#LISTAS
diagonal_principal = []
diagonal_secundaria = []
coluna = []
somas = []

for indice in range(tamanhoM):
    
    #LINHA
    somas.append(sum(entrada[inicio_linha:final_linha]))
    
    #DIAGONAL PRINCIPAL
    diagonal_principal.append(entrada[passo_dp])
    
    #DIAGONA SECUNDÁRIA
    diagonal_secundaria.append(entrada[passo_ds])

    #CONTADORES
    inicio_linha += tamanhoM
    final_linha += tamanhoM
    passo_dp += tamanhoM+1
    passo_ds += tamanhoM-1

    #COLUNAS
    for i in range(tamanhoM):
        coluna.append(entrada[indice])
        indice += tamanhoM
        
    somas.append(sum(coluna))
    coluna.clear() #Zerando lista da coluna para ser usada na próxima 

for i in somas:
    if i != sum(diagonal_principal):
        x = -1
        print(x)
        sys.exit()
print(sum(diagonal_principal)) #Poderia ser qualquer lista que guarde uma soma



