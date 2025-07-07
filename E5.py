a = []
cont = int(0)
s1 = int(0)
s2 = int(0)

for cont in range(3):
    print("Digite um número")
    a.append(int(input()))

    if(a[cont] %2 ==0):
        s1 = s1 + a[cont]
    else:
        s2 = s2 + a[cont]

print(f"A soma dos pares é {s1}\nA soma dos ímpares é {s2}")