s1= int(0)
s2 = int(0)

for cont in range(0,6,1):
    print("Digite um valor")
    a1 = int(input())
    if(a1 %2 == 0):
        s1 = s1 + 1
        s2 = s2 + a1
print(f"Foram digitados {s1} números pares\nA soma dos números é {s2}")