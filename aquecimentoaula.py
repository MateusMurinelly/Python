nomes = []
print('-'*30)
print('Bem vindo ao cadastra nome')
print('-'*30)

print('Digite [1] para adicionar usuarios\n''Digite [2] para visualizar cadastrados\n''Digite [3] para atualizar os valores\n''Digite [4] para deletar\n''Digite [5] para Sair')
op = input('digite a opção escolhida: ')


while True:
    if op == '1':
        nomes.append(input('Digite o novo usuario: '))
        op = input('digite a nova opção do menu escolhida: ')
    elif op == '2':
        print(nomes)
        if len(nomes) == 0:
            print('Essa lista está vazia!')
            op = input('digite a nova opção do menu escolhida: ')
        else:
            op = input('digite a nova opção do menu escolhida: ')
    elif op == '3':
        print(nomes)
        x = input('qual item deseja atualizar: ')
        if x not in nomes:
            print('\033[0;30;41mNOME NÃO CONSTA NA LISTA\033[m')
            continue
        else:
            y = input('digite o novo nome a ser cadastrado: ')
            z = nomes.index(x)
            nomes.pop(z)
            nomes.insert(z,y)
            print(nomes)
            op = input('digite a nova opção do menu escolhida: ')
    elif op == '4':
        print(nomes)
        x = input('qual NOME deseja deletar: ')

        if x not in nomes:
            print('\033[0;30;41mNOME NÃO CONSTA NA LISTA\033[m')
            continue
        else:
            y = nomes.index(x)
            nomes.pop(y)
            print(nomes)
            op = input('digite a nova opção do menu escolhida: ')
    elif op == '5':
        print(nomes)
        sair = input('\033[0;30;41mdeseja realmente sair?\n [s]para sim\n [n]para não: \033[m\n').lower()
        if sair == 's':
            print(f'Sua lista final é: {nomes}.')
            break
        elif sair == 'n':
            op = input('digite a nova opção do menu escolhida: ')
        else:
            print('\033[0;30;41mOPÇÃO INVALIDA\033[m')
            sair = input('deseja realmente sair?\n [s]para sim\n [n]para não: \n').lower()
    else:
        print('\033[0;30;41mOPÇÃO INVALIDA\033[m')
        op = input('digite a nova opção do menu escolhida: ')







