print("Que número você quer começar?")
a1 = int(input())
print("Qual o limite?")
a2 = int(input())
print("Quantas casas serão puladas?")
a3 = int(input())
c = int(0)

while(a1 < a2):
    a1 = a1 + a3
    print(f"{a1}")