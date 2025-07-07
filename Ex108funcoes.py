def avista(a):
    a = float(a * 0.9)
    print(f"O total ficou em R${a}")

def aprazo(a):
    a = int(a * 1.1)
    print("O total ficou em " + str(a))

def cartao(a,c):
    a1 = int(0)
    a1 = float((a * 1.2) / c)
    print(f"Sua compra de R${a} parceladas em {c} sendo um total de R${a1}")