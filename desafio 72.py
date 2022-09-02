cont = ('zero', 'um', 'dois', 'trés', 'quatro', 'cinco', 'seis')
while True:
     n = int(input('digite um numero de 0 a 6: '))
     if 0 <= n <= 6:
         break
print (f'o numero por extenso é {cont[n]}')
