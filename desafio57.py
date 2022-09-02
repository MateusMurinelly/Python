import random
numero = random.randint(0,10)
acertou = False
while not acertou:
    tentativa = int(input('digite um numero: '))
    if tentativa == numero:
        acertou = True
print ('acabou')