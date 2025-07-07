a = [0,0,0]
cont= int(0)
s1 = int(0)

for cont in range(3):
    print("Digite um número")
    a[cont] = int(input())
    if(a[cont] == 14):
        s1 = s1 +1

print(f"O número 14 aparece {s1} vezes")