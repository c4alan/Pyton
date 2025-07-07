a = []
cont = int(0)
s1 = int(0)
s2 = int(0)

for cont in range(3):
    print("Digite um número")
    a.append(int(input()))

    if(a[cont] %2 == 0):
        s1 = s1 +1
    else:
        s2 = s2 + 1

print(f"Foram encontrados {s1} números pares e {s2} números ímpares")