print("A que velocidade o carro estava?")
a1 = float(input())


if(a1 <= 80):
    print("Velocidade segura")
else:
    s1 = int(0)
    a1 = a1 *10 - 800
    s1 = 450 + a1 
    print("Sua multa é de " + str(s1))
