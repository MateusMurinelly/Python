print('Seja bem vindo!')
numero = int(input("Digite o numero o qual deseja saber o fatorial: ") )

resultado=1
count=1

while count <= numero:
    resultado *= count
    count += 1

print(f'O resultado da fatoração foi: {resultado}')
print ('Powered by Murinelly')
