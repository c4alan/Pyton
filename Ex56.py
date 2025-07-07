c = int(0)
s1 = int(0)
s2 = int(0)

while(c < 5):
    print("Digite um número")
    a1 = int(input())
    if(a1 % 2 == 0):
        s1 = s1 + a1
    if(a1 %2 == 1):
        s2 = s2 + a1
    c = c +1
print(f"A soma dos pares é {s1} e a soma dos ímpares é {s2}")