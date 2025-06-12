print("Digite um número")
a1 = int(input())
print("Digite outro número")
a2 = int(input())
print("Digite mais um número")
a3 = int(input())

s1 =int(0)
s2 = int(0)

if(a1 % 2 == 0):
    s1 = s1 + 1
else:
    s2 = s2 + 1

if(a2 % 2 ==0):
    s1 = s1 + 1
else:
    s2 = s2 + 1
if(a3 % 2 ==0):
    s1 = s1 + 1
else:
    s2 = s2  +1

print("Foram encontrados " + str(s1) + " números pares")
print("Foram encontrados " + str(s2) + " números ímpares")