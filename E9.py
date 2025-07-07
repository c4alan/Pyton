import Ex9funcoes

print("Qual o valor do produto?")
a = float(input())
print("Em qual feriado estamos?\n[1]Carnaval\n[2]Férias escolares\n[3]Dia das crianças\n[4]Black Friday\n[5]Natal")
a1 = int(input())

match a1:
    case 1:
        Ex9funcoes.carnaval(a,a1)
    case 2:
        Ex9funcoes.Fe(a,a1)
    case 3:
        Ex9funcoes.Dia(a,a1)
    case 4:
        Ex9funcoes.bf(a,a1)
    case 5:
        Ex9funcoes.nat(a,a1)