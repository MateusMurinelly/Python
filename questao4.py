from math import floor
print("Bem vindo")
valor = float(input('digite o valor da compra: '))

desconto = int
desconto = (valor / 100) - 4
descontob = floor(desconto)

valord = valor * (descontob / 100)
if descontob >= 25:
    descontob == 25
print(f'o valor da sua compra foi R${valor} e o desconto {descontob}%')
total = valor - valord
print(f'o total R${total}')



