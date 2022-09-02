print('Seja bem vindo')
print('Vamos verificar se um numero entre 0 e 100 é primo ou não ')
numero = int(input('Digite um numero numero: '))
indice = 0
while numero > 0 and numero < 101:

    for i in range(1, (numero + 1)):
        if numero % i == 0:
            indice += 1

    if indice == 2:
        print(f'O numero {numero} é primo')
        break
    else:
        print(f'O numero {numero} não primo')
        break
