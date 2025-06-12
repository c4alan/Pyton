print("Qual a sua divída?")
a1 = float(input())
print ("Qual o tempo dessa divída?")
a2 = float (input())
print("Qual a taxa de juros?")
a3 = int(input())

j1= float(a1 * a2 * (a3 / 100))
t1 = float(a1 + j1)

print("Os juros são " + str(j1) + " e o total será de " + str(t1))