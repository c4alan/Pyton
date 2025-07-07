c = int(0)
s1 = int(0)

while (c <200):
    c = c +1
    print("Digite um número")
    a1 = int(input())
    if(a1 > 0):
        s1 = s1 + a1
        if(s1 > 1000):
            s1 = s1 - 1000
            print(f"Você excedeu em {s1}")
            break