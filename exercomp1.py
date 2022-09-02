num1 = int(input('escreva o primeiro numero do intervalo: '))
num2 = int(input('escreva o segundo numero do intervalo: '))

for indice in range(num1, num2 + 1):
    if indice > 1:
        for x in range(2, indice):
            if (indice % x == 0):
                break
        else:
            print(indice)
