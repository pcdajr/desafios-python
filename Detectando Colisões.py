entrada  = input()
entrada = entrada.split()



if (entrada[:4] == entrada[4:]):
    print('1')
    
elif (entrada[:2] < entrada[4:5:1]) and entrada[2:3:1] >= entrada[4:]:
    print('1')

elif (entrada[:2] > entrada[4:5:1]) and entrada[2:3:1] <= entrada[4:]:
    print('1')

elif (entrada[:2] < entrada[4:5:1]) and entrada[2:3:1] >= entrada[4:]:
    print('1')
    
elif (entrada[6]!= entrada[7]):
    print('1')
    
else:
    print('0')

