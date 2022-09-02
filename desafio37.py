resphospital1 = int(input('digite o numero de respiradores do hospital1: '))
ocupaçãoh1 = float(input('digite a porcentagem de ocupação do hospital1: '))
resphospital2 = int(input('digite o numero de respiradores do hospital2: '))
ocupaçãoh2 = float(input('digite a porcentagem de ocupação do hospital2: '))
resphospital3 = int(input('digite o numero de respiradores do hospital3: '))
ocupaçãoh3 = float(input('digite a porcentagem de ocupação do hospital3: '))
resphospital4 = int(input('digite o numero de respiradores do hospital4: '))
ocupaçãoh4 = float(input('digite a porcentagem de ocupação do hospital4: '))
resphospital5 = int(input('digite o numero de respiradores do hospital5: '))
ocupaçãoh5 = float(input('digite a porcentagem de ocupação do hospital5: '))


while resphospital1 < 50 and ocupaçãoh1 >= 60:
    print('adicionar 5 respiradores hospital1')
    break
if resphospital2 < 50 and ocupaçãoh2 >= 60:
    print('adicionar 5 respiradores hospital2')

if resphospital3 < 50 and ocupaçãoh3 >= 60:
    print('adicionar 5 respiradores hospital3')

if resphospital4 < 50 and ocupaçãoh4 >= 60:
    print('adicionar 5 respiradores hospital4')

if resphospital5 < 50 and ocupaçãoh5 >= 60:
    print('adicionar 5 respiradores hospital5')


