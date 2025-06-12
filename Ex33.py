print("Digite o 1º número")
a1 = int(input())
print("Digite o 2º número")
a2 = int(input())
print("Digite o 3º número")
a3 = int(input())
print("Digite o 4º número")
a4 = int(input())

s1 = int(0)
s2 = int(0)
s3 = int(0)

if(a1 %2 == 0):
    s1= s1 + 1
    s2 = s2 + a1
if(a1 > s3):
    s3 =a1
if(a2 %2 == 0):
    s1 = s1 + 1
    s2 = s2 + a2
if(a2 > s3):
    s3 = a2
if(a3 %2 == 0):
    s1 = s1 + 1
    s2 = s2 + a3
if(a3 > s3):
    s3 = a3
if(a4 %2 ==0):
    s1 = s1 + 1
    s2 = s2 + a4
if(a4 > s3):
    s3 =a4

print("Foram digitados " + str(s1) + " números pares")
print("A soma desses números pares é " + str(s2))
print("O maior número par é " + str(s3))