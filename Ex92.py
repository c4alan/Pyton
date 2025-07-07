a=[0,0,0,0,0,0]
cont = int(0)
s1 = int(0)
s2 = int(999999999999999999)
s3 = int(0)

for cont in range(6):
    print("Digite sua nota")
    a[cont] = int(input())
    if(a[cont] > s1):
        s1 = a[cont]
    if(a[cont] < s2):
        s2 = a[cont]
    s3 = (s3 + a[cont])/6

print(f"A maior nota é {s1}\nA menor nota é {s2}\nA média é {s3}")
