n50 = int(0)
n20 = int(0)
n10= int(0)
n2 = int(0)
n1 = int(0)
print("Digite o valor")
valor= int(input())

while (valor > 0):
    if(valor >= 50):
        n50 = n50 + 1
        valor = valor - 50
    elif( valor >=20):
        n20 = n20 + 1
        valor = valor - 20
    elif(valor >= 10):
        n10 = n10 +1
        valor = valor - 10
    elif(valor >=2):
        n2 = n2 + 1
        valor = valor - 2
    elif (valor >= 1):
        n1 = n1 + 1
        valor = valor - 1

print(f"Você quer fazer um saque de {valor}\n{n50} notas de R$50,00\n{n20} notas de R$20,00\n{n10} notas de R$10,00\n{n2} notas de R$2,00\n{n1} nota de R$1,00")