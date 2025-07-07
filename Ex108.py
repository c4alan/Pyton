import Ex108funcoes

print("Qual o valor da sua compra?")
a= float(input())
print("Como foi feito o pagamento:\n[1]A vista\n[2]Parcelado\n[3]Cartão/Parcelado")
b = int(input())

match b:
    case 1 :
        Ex108funcoes.avista(a)
    case 2:
        Ex108funcoes.aprazo(a)
    case 3:
        print("Quantas vezes vai parcelar?")
        c = int(input())
        Ex108funcoes.cartao(a,c)

