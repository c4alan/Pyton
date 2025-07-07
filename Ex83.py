a1 = int(0)
a2 = int(0)
a3 = int(1)

print("Digite um número")
a1 = int(input())


while(a3 <= a1):
    if(a1 % a3 ==0):
        a2 = a2 + 1
    a3 = a3 + 1

if(a2 == 2):
        print("é primo")
else:
        print("Não é primo")

