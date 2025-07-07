s1 = int(0)
s2= int(0)

for cont in range(0,9,1):
    print("Escreva um número")
    a = int(input())
    s1 = s1 + 1
    s2 = s2 + a
    if(a == 999):
        print("Conseguiu!")
        print(f"A soma dos números é {s2} e foram feitas {s1} tentativas")
        break
print(f"A soma dos números é {s2} e foram feitas {s1} tentativas")

