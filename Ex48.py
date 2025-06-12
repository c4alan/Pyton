print("Qual série você assistiu final de semana \n[1]Sandman\n[2]Wandinha\n[3]Game of Thrones\n[4]Dota\n[5]Dexter")
a1 = int(input())

match a1:
    case 1:
        print("A série escolhida foi Sandman")
    case 2:
        print("A série escolhida foi Wandinha")
    case 3:
        print("A série escolhida foi Game of Thrones")
    case 4:
        print("A série escolhida foi Dota")
    case 5:
        print("A série escolhida foi Dexter")
    case _:
        print("ERRO")