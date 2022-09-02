print('olá seja bem vindo')
salario = float(input('digite o valor do seu salario atualmente: R$'))
salarion = float
if salario < 280:

    salarion = salario + (salario * 0.2)
if salario > 280 <= 700:

    salarion = salario + (salario * 0.15)

if salario > 700 <= 1500:

    salarion = salario + (salario * 0.1)
if salario > 1500:

    salarion = salario + (salario * 0.05)
print(f'seu novo salario será R${salarion}')
