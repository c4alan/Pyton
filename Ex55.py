print("Até que número você quer contar?")
a1 = int(input())
c = int(0)

while (c < a1):
    c = c + 1
    print(f"{c}--",end="")
    if(c % 3 ==0):
        print("Pin \n")