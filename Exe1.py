#array -> vetor
#cadeia a[4] = {"Joaquim,","23","rua a","40"}

a = ["Joaquim",22,"Rua a",40]

print(a)
print(a[0])
print(a[1])
print(a[2])
print(a[3])

print("____________________")

cont = int(0)

#Uma forma de abreviar o for se pular de 1 em 1 é colocando for cont in range(x) x-> número de casas
for cont in range (4):
    print(a[cont])

for k in a:
    #interar o vetor
    print(k)
    #soma = soma + k(k tem que ser número)

ze = len(a)
print(ze)

#métodos -> são rotinas que pertencem a um elemento
a.append("pedro")