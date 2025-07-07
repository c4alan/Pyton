import Ex11funcoes

print("Escolha um humorista:\n[1]Fabio Porchat\n[2]Danilo Gentili\n[3]Rafinha Bastos")
a = int(input())

match a:
    case 1:
        t=Ex11funcoes.FB(a)
        print(f"Você tem {t[0]} anos e mora na cidade {t[1]}")
    case 2:
        t = Ex11funcoes.DG(a)
        print(f"Sua altura é {t[0]} e seu peso é {t[1]}")
    case 3:
        t= Ex11funcoes.RB(a)
        print(f"A cor do seu cabelo é {t[0]} e sua altura é {t[1]}")
         