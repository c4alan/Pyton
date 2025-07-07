print("Qual o valor do produto?")
a1 = float(input())
print("Qual a forma de pagamento?")
a2 = str(input())
s1 = float(0)

if(a2 == "Pix"):
    s1=  a1 - a1 * 0.1
if(a2 == "Débito"):
    s1= a1 - a1*0.05
if(a2 == "Crédito"):
    print("Em quantas vezes parcelou?")
    a4 = int(input())
    if(a4 <3):
        s1 = a1 + a1 * 0.05
        s2 = float(a1 /a4)
        print(f"Sua compra de {a1} parcelada em {a4} de {s2} com um acréscimo de 5% ficando em R${s1}")
    if(a4 > 3):
        s1 = a1 + a1 * 0.1
        s2 = float(a1 / a4)
        print(f"Sua compra de {a1} parcelada em {a4}x de {s2} com acréscimo de 10% ficando em R${s1}")