print('seja bem vindo')
dia = int(input('digite o dia do seu nascimento: '))
mes = str(input('escreva o nome do mês do seu nascimento:'.lower()))
while dia >= 1 and dia <= 30:

    if dia >= 21 and mes == 'março' or dia <= 20 and mes == 'abril':
        print('seu signo é aries')
        break
    if dia >= 21 and mes == 'abril' or dia <= 20 and mes == 'maio':
        print('seu signo é touro')
        break
    if dia >= 21 and mes == 'maio' or dia <= 20 and mes == 'junho':
        print('seu signo é gêmeos')
        break
    if dia >= 21 and mes == 'junho' or dia <= 22 and mes == 'julho':
        print('seu signo é câncer')
        break
    if dia >= 23 and mes == 'julho' or dia <= 22 and mes == 'agosto':
        print('seu signo é leão')
        break
    if dia >= 23 and mes == 'agosto' or dia <= 22 and mes == 'setembro':
        print('seu signo é virgem')
        break
    if dia >= 23 and mes == 'setembro' or dia <= 22 and mes == 'outubro':
        print('seu signo é libra')
        break
    if dia >= 23 and mes == 'outubro' or dia <= 21 and mes == 'novembro':
        print('seu signo é escorpião')
        break
    if dia >= 22 and mes == 'novembro' or dia <= 21 and mes == 'dezembro':
        print('seu signo é sargitário')
        break
    if dia >= 22 and mes == 'dezembro' or dia <= 20 and mes == 'janeiro':
        print('seu signo é capricórnio')
        break
    if dia >= 21 and mes == 'janeiro' or dia <= 18 and mes == 'fevereiro':
        print('seu signo é aquário')
        break
    if dia >= 19 and mes == 'fevereiro' or dia <= 20 and mes == 'março':
        print('seu signo é peixes')
        break
print('powered by Murinelly')