print("Qual sua idade?")
a1 = int(input())
print("Qual sua nacionalidade?")
a2 = str(input())
print("Qual o seu sexo?")
a3 = str(input())

if(a1 == 18 and a2 == "Brasileiro" and a3 == "Masculino"):
    print("Apto")
else:
    print("Não apto")