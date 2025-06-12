print("Digite a 1ª nota")
a1 = int(input())
print("Digite a 2ª nota")
a2 = int(input())
print("Digite a 3ª nota")
a3 = int(input())
print("Digite a 4ª nota")
a4 = int(input())

s1 = int((a1 + a2 + a3 + a4) / 4)

if(s1 >= 7):
    print("Aprovado!")
else:
    print("Reprovado")