print("Digite o 1º número")
a1 = int(input())
print("Digite o 2º número")
a2 = int(input())
print("Digite o 3º número")
a3 = int(input())

s1 = int(0)
s2 = int(0)

if(a1 % 2 ==0):
    s1 = s1 + a1
else:
    s2 = s2 + a1

if(a1 %2 == 0):
    s1 = s1 + a1
else:
    s2 = s2 + a1

if(a1 %2 == 0):
    s1 = s1 + a1
else:
    s2 = s2 + a1

print("A soma dos números pares é " + str(s1))
print("A soma dos números ímares é " + str(s2))