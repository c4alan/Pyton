import random
a1 = float(0)
a2 = float(0)
a = ["Vermelho","Preto","Preto","Vermelho","Branco","Preto"]
a3 = random.randint(0,5)
a4 = str("")

print("Qual seu saldo bancário?")
a1 = int(input())
print("Quanto você deseja apostar?")
a2 = int(input())

if(a2 > a1):
    print("Saldo insuficiente")
else:
    print("Qual cor você deseja apostar?")
    a4 = input()
    print(f"Foi sorteado a cor {a[a3]}")
    if(a[a3] == "Vermelho" and a4 == "Vermelho"):
            a2 = a2 *2
            a1 = a1 + a2
    if(a[a3] == "Branco" and a4 == "Branco"):
            a2 = a2 * 14
            a1 = a1 + a2
    if(a[a3] == "Preto" and a4 == "Preto"):
            a2 = a2 * 2
            a1 = a1 + a2
    if(a[a3] != a4):
            print("PERDEU!")
            a1 = a1 - a2
    print(f"Seu saldo final é {a1}")
