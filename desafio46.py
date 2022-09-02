import time
inicio = int(input('digite o inicio da contagem:'))
fim = int(input('digite o final:'))
for c in range(inicio,fim,-1):
    print (c)
    time.sleep(1)
print ('FIM')


