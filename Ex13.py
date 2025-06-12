print("Digite o 1º valor")
a1= int(input())
print("Digite o 2º valor")
a2= int(input())
print("Digite o 3º valor")
a3= int(input())
s1 = int(0)

if(a1 > 25):
    s1 = s1 + 1
if(a2 > 25):
    s1 = s1 + 1
if(a3 > 25):
    s1 = s1 + 1

print ("Encontramos " + str(s1) + " números maiores do que 25")