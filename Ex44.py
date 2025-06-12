print("Quanto você vendeu?")
a1 = float(input())

if(a1 >= 22000):
    print("Quantos anos você tem de empresa?")
    a2= int(input())
    if(a2 == 2):
        s1 =  a1 * 0.03
        print("Sua comissão será de " + str(s1))
    if(a2 >= 3):
        s1 =  a1 * 0.04
        print("Sua comissão será de " + str(s1))
    if(a2 <2 ):
        s1 =  a1 * 0.02
        print("Sua comissão será de " + str(s1))
        