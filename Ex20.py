print("Digite um número")
a1 = int(input())
print("Digite outro número")
a2 = int(input())
print("Você quer saber a soma ou a média")
a3 = str(input())

if(a3 == "Média"):
    s1 = int(0)
    s1 = (a1 + a2) /2
    print("A média de " + str(a1) + " + " + str(a2) + " é igula á " + str(s1))

if(a3 == "Soma"):
    s2 = int(0)
    s2 = (a1 + a2)
    print("A soma de " + str(a1) + " + " + str(a2) + " é igual a " + str(s2))