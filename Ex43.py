print("Quantos anos você tem?")
a1 = int(input())
if(a1 == 18):
    print("Qual o seu sexo?")
    a2 = str(input())
    if(a2 == "masculino"):
        print("Qual sua nacionalidade")
        a3 = str(input())
        if(a3 == "brasileiro"):
            print("Bem vindo soldado")
        else:
            print("Dispensado")
    else:
        print("Dispensado")
else:
    print("Dispensado")