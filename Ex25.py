print("Qual a velocidade do carro?")
a1= float(input())


if(a1 > 280):
    print("Seu veiculo será confiscado")
if(a1 <= 80):
    print("Velociade segura")

if(a1 > 80 and a1 <= 100):
    s1 = int(0)
    a1 = a1 * 5 - 400
    s1 = 150
    s2 = s1 + a1
    print("Velocidade excedida. Sua multa é " + str (s2))
if(a1 > 100 and a1 <= 160):
    s1 = int(0)
    a1 = a1  * 10 - 1000
    s1 = 250 + a1
    print("Limite de velocidade excedido " + str(s1))
if(a1 > 160 and a1 < 280):
    s1 = int(0)
    a1 = a1 * 20 - 3200
    s1 = 500 + a1
    print("Sua multa é de  " + str(s1))
