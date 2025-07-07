a = []
cont = int(0)
s1 = float(0)
s2 = int(0)

for cont in range(3):
    print("Qual o valor de suas compras?")
    a.append(float(input()))
    s1 = s1 + a[cont]
    s2 = s1/3
    
if(s1 > s2 *2):
    print("Verdadeiro")
else:
    print("Falso")
print(a)