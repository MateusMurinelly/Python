tabela = ('ferroviario','fortaleza','ceara','icasa','horizonte','palhano')

opção = int(input('digite sua opção: '))
if opção == 1:
    print(f'os 5 primeiros são {tabela[0:5]}')
if opção == 2:
    print(f'os 4 ultimos são {tabela[-4:]}')
if opção == 3:
    print(f'em ordem alfabetica fica: {sorted(tabela)}')
else:
    print('fim')

