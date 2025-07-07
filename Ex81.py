import random
a1 = random.randint(0,999)
a2 = int()
while(a2 != a1):
    print("Digite um número")
    a2 = int(input())
    if(a2 > a1):
        print("Tente um número menor")
    if(a2 < a1):
        print("Tente um número maior")
    if(a2 == a1):
        print("Acertou")