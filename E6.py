a = []
cont = int(0)
s1 = int(0)
s2 = int(0)
s3 = int(0)

for cont in range(4):
    print("Digite um número")
    a.append(int(input()))

    if(a[cont] %2 == 0):
        s1 = s1 +1
        s2 = s2 + a[cont]
    
    if(a[cont] %2 == 0 and a[cont] > s3):
        s3 = a[cont]

print(f"Foram digitados {s1} números pares\nA soma desses números pares é {s2}\nO maior número par é {s3}")