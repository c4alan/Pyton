print ("Qual sua idade?")
a1 = int(input())
print("Você fala inglês?")
a2 = str(input())

if(a2 == "Sim"):
    print("Verdadeiro")
elif(a2 == "Sim" and a1 > 25):
    print("Verdadeiro")
else:
    print ("Falso")