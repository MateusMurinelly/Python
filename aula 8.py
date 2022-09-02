numero = int(input('digite seu numero: '))

print('seu numero é {}'.format(numero))
u = numero // 1 % 10
print('seu numero tem {} unidades'.format(u))
d = numero // 10 % 10
print ('seu numero tem {} dezenas'.format(d))
c = numero // 100 % 10
print ('seu numero tem {} centenas'.format(c))
m = numero // 1000 % 10
print ('por fim seu numero tem {} milhares'.format(m))