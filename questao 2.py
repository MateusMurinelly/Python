print("Bem vindo")

faixa1 = 0
faixa2 = 0
faixa3 = 0
faixa4 = 0
faixa5 = 0

pessoas = 0
while pessoas <= 14:
    idade = int(input("digite a idade: "))

    if idade <= 15:
        faixa1 = faixa1 + 1
        pessoas = pessoas + 1

    if idade >= 16 and idade <= 30:
        faixa2 = faixa2 + 1
        pessoas = pessoas + 1

    if idade >= 31 and idade < 45:
        faixa3 = faixa3 + 1
        pessoas = pessoas + 1

    if idade >= 46 and idade <= 60:
        faixa4 = faixa4 + 1
        pessoas = pessoas + 1

    if idade >= 61:
        faixa5 = faixa5 + 1
        pessoas = pessoas + 1

print("pessoas na faixa 1: ", faixa1)
print("pessoas na faixa 2: ", faixa2)
print("pessoas na faixa 3: ", faixa3)
print("pessoas na faixa 4: ", faixa4)
print("pessoas na faixa 5:", faixa5)
porcentagem = float(faixa1 + faixa5) / (faixa1 + faixa2 + faixa3 + faixa4 + faixa5)
print("total percentual das faixas 1 e 5 em relação ao total:", porcentagem * 100,"%")