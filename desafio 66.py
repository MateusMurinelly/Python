

n = s = 0
cont = s

while True:
    n = int(input('digite um valor '))
    if n == 999:
        break
    s += n
    cont += 1

print(f'a soma dos {cont} valores é {s}')