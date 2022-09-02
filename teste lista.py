lista = []
maior = 0
menor = 0
for c in range(0,6):
    lista.append(int(input(f'digite um valor {c}:')))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]
print(f'voce digitou esses valores{lista}')
print(f'o maior valor é {maior}')
print(f'o menor valor é {menor}')