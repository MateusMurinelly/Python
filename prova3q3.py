comandos = ['frente','direita','esquerda','parar']
d = 0
usuario = str(input('digite o comando dentre (frente,direita,esquerda ou parar): '))
while usuario != 'parar':
    usuario = str(input('digite o comando dentre (frente,direita,esquerda ou parar): '))
    d = d + 100

print(f'A distancia percorrida foi de {d/1000}Km')