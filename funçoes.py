def linha(x):
    return '-' * x


def op1(nomes):
    nomes.append(input('Digite o novo usuario: '))
    op = input('digite a nova opção do menu escolhida: ')
    return int(op)


def op2(nomes):
    print(nomes)
    while len(nomes) == 0:
        print('Essa lista está vazia!')
        op = input('digite a nova opção do menu escolhida: ')
        return int(op)
    else:
        op = input('digite a nova opção do menu escolhida: ')
        return int(op)


def op3(nomes):
    print(nomes)
    while True:
        x = input('qual item deseja atualizar: ')
        if x not in nomes:
            print('\033[0;30;41mNOME NÃO CONSTA NA LISTA\033[m')
            continue
        else:
            y = input('digite o novo nome a ser cadastrado: ')
            z = nomes.index(x)
            nomes.pop(z)
            nomes.insert(z, y)
            print(nomes)
            op = input('digite a nova opção do menu escolhida: ')
            return int(op)


def op4(nomes):
    print(nomes)
    while True:
        x = input('qual NOME deseja deletar: ')
        if x not in nomes:
            print('\033[0;30;41mNOME NÃO CONSTA NA LISTA\033[m')
            continue
        else:
            y = nomes.index(x)
            nomes.pop(y)
            print(nomes)
            op = input('digite a nova opção do menu escolhida: ')
            return int(op)


def op5(nomes):
    print(nomes)
    sair = input('\033[0;30;41mdeseja realmente sair?\n [s]para sim\n [n]para não: \033[m').lower()
    while sair != 's' or sair != 'n':
        if sair == 's':
            print(f'Sua lista final é: {nomes}.')
            op = 'australopitecos'
            return op
        elif sair == 'n':
            op = input('digite a nova opção do menu escolhida: ')
            return int(op)
        else:
            print('\033[0;33mOPÇÃO INVALIDA\033[m')
            sair = input('\033[0;30;41mdeseja realmente sair?\n [s]para sim\n [n]para não: \033[m').lower()