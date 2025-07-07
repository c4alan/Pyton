import Ex115funcoes

print("Qual o seu saldo bancário?")
a = float(input())
print("Em qual moeda você quer converter?\n[1]Dolár\n[2]Euros\n[3]Ienes")
a1 = int(input())

match a1:
    case 1:
        t= Ex115funcoes.dolar(a,a1)
        print(f"Você tem equivalente a {t} Doláres")
    case 2:
        t2 = Ex115funcoes.euro(a,a1)
        print(f"Você tem equivalente a {t2} Euros")
    case 3:
        t3 = Ex115funcoes.iene(a,a1)
        print(f"Você tem equivalente a {t3} Ienes")