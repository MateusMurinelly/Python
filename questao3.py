print("Bem vindo")

nota1 = float(input('digite sua nota AV1: '))
nota2 = float(input('digite sua nota AV2: '))
nota3 = float(input('digite sua nota AV3: '))
presenca = int(input('digite sua presença: '))

notafinal = float((nota1 + nota2 + nota3)/3)
if notafinal >= 6 and presenca >= 40:
    print('parabens vc foi aprovado!')
else:
    print(f'sua media foi {notafinal:.2f} e sua presença foi {presenca}')
    print("Você foi REPROVADO")

