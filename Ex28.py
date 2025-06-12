print("Digite o 1º salario")
a1 = float(input())
print("Digite o 2º salario")
a2 = float(input())
print("Digite o 3º salario")
a3 = float(input())
print("Digite o 4º salario")
a4 = float(input())

s1 = int(0)

if(a1 > s1):
    s1 = a1
if(a2 > s1):
    s1 = a2
if(a3 > s1):
    s1 = a3
if(a4 > s1):
    s1 = a4

print("O maior salario entre as pessoas é " + str(s1))