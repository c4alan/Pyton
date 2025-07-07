a = [0,0,0,0]
a1 = [0]
cont = int(0)
s1 = int(0)
s2 = int(0)
s3 = int(0)


for cont in range(4):
    print("Digite um número")
    a[cont]= int(input())
    if(a[cont] %2 == 0):
        s1 = s1 + 1
        s2 = s2 + a[cont]
print("Os seguintes números são ímpares")
for cont in range(4):
    if(a[cont] %2 == 1):
        print(a[cont])

print(f"A soma dos pares é {s2}")