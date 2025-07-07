a1 = float(0)
a2 = float(0)
a3 = float(0)
import random

print("Qual seu saldo bancário?")
a1 = float(input())
print("Quanto você quer apostar?")
a2 = float(input())
for cont in range(2):
    cont = cont + 1
    if(a2 > a1):
        print("Saldo insuficiente!")
        break
    elif(cont >=0 and cont <= 1 and a1 > a2):
        print("Escolha um multiplicador")
        a3 = float(input())
        if(a3 == 1.1):
            b = random.randint(0,9)
            if(b >=0 and b <=9):
                a2 = a2 * 1.1
            else:
                a1 = a1 - a2
        if(a3 == 1.3):
            a =[1.3,1.3,1.3,1.3,1.3,1.3,1.3,1.3,1.3,1.3]
            b = random.randint(0,9)
            if(a[b] == 1.3):
                a2 = a2 * 1.3
                a1 = a1 + a2
            else:
                a1 = a1 - a2
        if(a3 == 1.6):
            a =[1.6,1.6,1.6,1.6,1.6,1.6,1.6,1.6,1.6,1.6]
            b= random.randint(0,9)
            if(a[b] == 1.6):
                a2 = a2  * 1.6
                a1 = a1 + a2
            else:
                a1 = a1 - a2
        if(a3 == 2):
            a=[2,2,2,2,2,2,2,2,2,2]
            b= random.randint(0,9)
            if(a[b] == 2):
                a2 = a2 *2
                a1 = a1 +a2
            else:
                a1 = a1 - a2
        if(a3 == 2.5):
            a = [2.5,2.5,2.5,2.5,2.5,2.5,2.5,2.5,2.5,2.5]
            b = random.randint(0,9)
            if(a[b] == 2.5):
                a2 = a2 * 2.5
                a1 = a1 + a2
            else:
                a1 = a1 - a2
        print(f"Seu saldo final é {a1}")
    else:
        print("Escolha um multiplicador")
        a3 = float(input())
        if(a3 == 1.1):
            b = random.randint(0,9)
            if(b >=0 and b <=8):
                a2 = a2 * 1.1
            else:
                a1 = a1 - a2
        if(a3 == 1.3):
            a =[1.3,1.3,1.3,1.3,1.3,1.3,1.3,1.3,0,0]
            b = random.randint(0,9)
            if(a[b] == 1.3):
                a2 = a2 * 1.3
                a1 = a1 + a2
            else:
                a1 = a1 - a2
        if(a3 == 1.6):
            a =[1.6,1.6,1.6,1.6,1.6,0,0,0,0,0]
            b= random.randint(0,9)
            if(a[b] == 1.6):
                a2 = a2  * 1.6
                a1 = a1 + a2
            else:
                a1 = a1 - a2
        if(a3 == 2):
            a=[2,2,2,2,0,0,0,0,0,0]
            b= random.randint(0,9)
            if(a[b] == 2):
                a2 = a2 *2
                a1 = a1 +a2
            else:
                a1 = a1 - a2
        if(a3 == 2.5):
            a = [2.5,2.5,0,0,0,0,0,0,0,0]
            b = random.randint(0,9)
            if(a[b] == 2.5):
                a2 = a1 * 2.5
                a1 = a1 + a2
            else:
                a1 = a1 - a2
        print(f"Seu saldo final é {a1}")        