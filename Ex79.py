c = str("")
s1 = int(0)
s2 = int(0)
s3 = int(0)
c1= int(0)

while(c != "sim"):
    print("Digite o nome do cliente")
    a1 = str(input())
    print("Digite o valor gasto")
    a2 = float(input())
    c1 = c1 + 1
    if(a2 > 1000):
        s1 = s1 +1
    if(a2 > 499 and a2 <999.99):
        s2 = s2 + 1
    if(a2 < 499.99):
        s3 = s3 + 1
    if(c1 >= 4):
        print("Deseja fechar o caixa")
        c = input()
        if(c == "sim"):
            print(f"Foram localizados {s1} clientes do tipo A\nForam localizados {s2} clientes do tipo B\nForam localizados {s3} clientes do tipo C")
            break