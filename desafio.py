import random
num = random.randint(0,5)
jogador = int(input('digite um numero:'))
if jogador == num:
    print('muito bem')
else:
    print('tente novamente')