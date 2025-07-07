import Ex8funcoes

print("Que série você viu final de semana?\n[1]Sandman\n[2]Sex Education\n[3]Game of Thrones\n[4]Dota\n[5]This is us")
a = int(input())

match a:
    case 1:
        Ex8funcoes.sand(a)
    case 2:
        Ex8funcoes.SE(a)
    case 3:
        Ex8funcoes.gth(a)
    case 4:
        Ex8funcoes.dot(a)
    case 5:
        Ex8funcoes.thi(a)
