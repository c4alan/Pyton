print("digite um número")
a1 = int(input())
print("Digite outro número")
a2 = int(input())
print("Digite mais um número")
a3 = int(input())

maior = int(0)
meio = int(0)
menor= int(0)
if(a1 > a2 and a1 > a3 and a2 > a3):
    maior = a1
    meio = a2
    menor=a3

if(a1 > a2 and a1 > a3 and a2> a3):
    maior = a1
    meio = a3
    menor = a2

if(a2 > a1 and a2 > a3 and a1>a3):
    maior = a2
    meio= a1
    menor= a3
if(a2 > a1 and a2 > a3 and a3 > a1):
    maior = a2
    menor = a3
    menor =a1

if(a3 > a1 and a3 > a2 and a1 > a2):
    maior= a3
    meio =a1
    menor= a2
if(a3 > a1 and a3 > a2 and a2 >a1):
    maior = a3
    meio = a2
    menor =a1
if(a1 == a2 and a1 == a3 and a2 == a1 and a2 == a3 and a3 == a2 and a3 == a1):
    print("Números iguais")
else:
    print("O maior é " + str(maior) + " e o menor é " + str(menor) + " e do meio é " + str(meio))