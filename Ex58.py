c = int(0)
s1 = int(0)
s2 = int(0)

while (c <7):
    c = c + 1
    print("Digite um número")
    a1 = int(input())
    if(a1 %3 ==0):
        s1 = s1 +1
    if(a1 %5==0):
        s2 = s2 + 1

print(f"Foram identificados {s1} números múltiplos de 3\nForam identificados {s2} números múltiplos de 5")