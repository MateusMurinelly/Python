imovel = float(input('Qual o valor do imovel:R$ '))
salario = float(input('Qual seu salario:R$ '))
parcelas = int(input('em quantas parcelas será: '))
valorp = imovel / parcelas
minimo = salario * 30/100

if valorp > minimo:
    print('O seu salario não é compativel com a parcela')
else:
    print('boa sorte na sua casa nova')
