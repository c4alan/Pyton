print("Digite um número")
a1 = int(input())
print("Digite outro número")
a2 = int(input())

s1 = int(0)
s2 = int(99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)

if(a1 > s1):
    s1 = a1
if(a1 < s2):
    s2 = a1
if(a2 > s1):
    s1 = a2
if(a2 < s2):
    s2 = a2

if(a1 == a2):
    print("Números iguais")
else:
    print("O maior número é " + str(s1) + " e o menor é " + str(s2))