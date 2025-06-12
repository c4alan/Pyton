print("Qual o valor da 1ª compra?")
a1 = float(input())
print("Qual o valor da 2ª compra?")
a2 = float(input())
print("Qual o valor da 3ª compra?")
a3= float(input())

s1= float(a1 + a2+ a3)
s2 = float ((a1 + a2 + a3)/3)

if(s1 > s2 * 2):
    print("Verdadeiro")
else:
    print("Falso")