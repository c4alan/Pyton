print("Digite seu peso")
a1 = float(input())

print("Escolha um planeta \n[1]Mercurio\n[2]Vênus\n[3]Marte\n[4]Jupiter\n[5]Saturno\n[6]Urano")
a2 = int(input())

match a2:
    case 1:
        s1 = float(a1 * 0.37)
        print("Seu peso em Mercurio é " + str(s1))
    case 2:
        s1 = float(a1 * 0.88)
        print("Seu peso em Vênus é " + str(s1))
    case 3:
        s1 = float(a1 * 0.38)
        print("Seu peso em Marte é " + str(s1))
    case 4:
        s1 = float(a1 * 2.64)
        print("Seu peso em Júpiter é " + str(s1))
    case 5:
        s1 = float(a1* 1.15)
        print("Seu peso em Saturno é " + str(s1))
    case 6:
        s1 = float(a1 * 1.17)
        print("Seu peso em Urano é " + str(s1))
    case _:
        print("Inválido")