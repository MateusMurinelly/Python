print('Olá seja bem vindo')
valorh = float(input('digite o valor da sua hora trabalhada: '))
quanth = float(input('digite a quantidade de horas trabalhadas: '))
salario = valorh * quanth
inss = 0.1
sindicato = 0.03

print(salario)
salariob = 0
if salario < 900:
    print('isento de IR')
elif salario == 900 < 1500:
    print('desconto de 5% de IR')
    salariob = salario * 0.05
elif salario > 1500 == 2500:
    print('desconto de 10% de IR')
    salariob = salario * 0.1
else:
    print('desconto de 20% de IR')
    salariob = salario * 0.2
print(salariob)
inss = salario * 0.1
print('desconto de inss', inss)
sind = salario * 0.03
print('desconto sindicato', sind)
dtotal = (salariob + inss + sind)
fgts = salario * 0.11
print(f'desconto total: {dtotal}')
salariol = salario - dtotal
print(f'seu salario ficou {salariol}')




