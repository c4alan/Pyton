print("Digite o valor do produto")
a1 = float(input())
print("Qual a forma de pagamento?")
a2 = str(input())

if(a2 == "dinheiro" or a2 == "pix"):
    s1 = a1 - a1 * 0.15
    print("O valor ficou em " + str(s1))

if(a2 == "crédito"):
    s2 = a1 - a1 * 0.1
    print("O valor ficou em " + str(s2))

if(a2 == "parcelar"):
    print("Em quantas vezes vai parcelar?")
    a3 = int(input())
    if(a3 == 2):
        print("O valor é " + str(a1))
    if(a3 >= 3):
        s3 = a1 + a1 * 0.1
        print("O valor ficou em " + str(s3))