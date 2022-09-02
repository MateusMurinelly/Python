velo = int(input('velocidade do veiculo: '))
if velo < 60:
    print('vocé esta dentro do limite permitido, \033[0;32m BOA VIAGEM \033[m')
elif velo == 60:
    print('você está no limite, \033[0;33m CUIDADO \033[m')
else:
    print('você esta acima do limite, sua multa tem valor de \033[0;31m R$ 895,00\033[m')
