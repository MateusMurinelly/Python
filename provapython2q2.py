print('seja bem vindo')
anos = int(input('digite quantos anos você tem: '))
meses = int(input('digite seu mês de nascimento (em numeros): '))
dias = int(input('digite seu dia de nascimento: '))
anosd = anos * 365
mesesd = meses * 30
total = anosd + mesesd + dias
print(f'O seu total de tempo de vida em dias é {total}')