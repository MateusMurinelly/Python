print("Bem vindo")
numero = int(input("digite o numero de moradores: "))
M = 0
F = 0
moradores = 1
while moradores <= numero:
    sexo = int(input("digite 1 para Masculino ou 2 para Feminino: "))
    if sexo == 1:
        M = M + 1
        moradores = moradores + 1
        print("sexo masculino ")
    if sexo == 2:
        F = F + 1
        moradores = moradores + 1
        print("sexo masculino ")


print("numero de moradores = ", numero)
print("numero de individuos do sexo masculino =", M)
print("numero de individuos do sexo masculino =", F)