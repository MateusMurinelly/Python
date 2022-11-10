#Menu de cadastro de nomes
from funçoes import op1,op2,op3,op4,op5
def linha(x):
    return '-' * x


nomes = []
print(linha(42))
print('Bem vindo ao cadastra nome'.center(42))
print(linha(42))

print(
    'Digite [1] para adicionar usuarios\n''Digite [2] para visualizar cadastrados\n''Digite [3] para atualizar os nomes\n''Digite [4] para deletar\n''Digite [5] para Sair')
print(linha(42))
op = input('digite a opção escolhida: ')

op = int(op)
while True:

    if op == 1:
        op = op1(nomes)
        print(linha(42))
    elif op == 2:
        op = op2(nomes)
        print(linha(42))
    elif op == 3:
        op = op3(nomes)
        print(linha(42))
    elif op == 4:
        op = op4(nomes)
        print(linha(42))
    elif op == 5:
        op = op5(nomes)
    elif op == 'australopitecos':
        break
    else:
        print('\033[0;30;41mOPÇÃO INVALIDA*****\033[m')
        op = int(input('digite a nova opção do menu escolhida: '))

