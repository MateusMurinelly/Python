quantv = int(input('digite a quantidade de vazamentos notificados: '))
n = 0
x = 0
while n < quantv:
    litros = float(input('vazão do vazamento em Litros/Hora: '))
    tempo = float(input('tempo de vazamento: '))
    totalL = litros * tempo
    x = x + totalL
    n += 1

print(f'O total de litros de água desperdiçada: {x}L')