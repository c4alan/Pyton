a = []
cont= int(0)
s1 = int(0)

for cont in range(4):
    print("Digite um salário")
    a.append(float(input()))
    if(a[cont] > s1):
        s1 = a[cont]

print(f"O maior salário entre as pessoas citadas é R${s1}")