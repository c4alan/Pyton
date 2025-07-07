c = str("")
s2 = int(0)
while (c != "Ganhou"):
    print("Digite um número")
    a = int(input())
    print("Você quer par ou ímpar")
    b = str(input())
    import random
    a1 = random.randint(0,9)
    s1 = int(0)
    s1 = a1 + a
    if(b == "par" and s1 %2 ==0):
        c = "Ganhou"
        print(c)
        break

    if(b == "ímpar" and s1%2 == 1):
        c = "ganhou"
        print(c)
        break
    
    if(b == "par" and s1 %2  ==1 or b == "ímpar" and s1%2 ==0):
        s2 = s2 +1

print(f"Você perdeu {s2} vezes")