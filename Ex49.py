print("Escolha um humorista \n[1]Fabio Porchat\n[2]Danilo Gentili\n[3]Rafinha Bastos")
a1 = int(input())
print("Qual sua cidade?")
a2 = str(input())

match a1:
    case 1:
        if(a2 == "Araxá"):
            print("Tem show do Fabio Porchat")
    case 2:
        if(a2 == "São Paulo"):
            print("Tem show do Gentili")
    case 3:
        if(a2 == "Rio Grande do Sul"):
            print("Tem show do Rafinha")