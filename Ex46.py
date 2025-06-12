print("Digite um número")
a1 =  int(input())
print("Digite outro número")
a2 = int(input())

print("Escolha uma operação \n[1]Soma\n[2]Subtração\n[3]Multiplicação\n[4]Divisão")
a3 = int(input())

match a3:
    case 1:
        s1 = int(a1 + a2)
        print("A soma de " + str(a1) + " + " + str(a2) + " é " + str(s1))
    case 2:
        s1 = int(a1 - a2)
        print("A subtração é igual a " + str(s1))
    case 3:
        s1= int(a1 * a2)
        print("A multiplicação é " + str(s1))
    case 4:
        s1 = float(a1 / a2)
        print("A divisão é igual a " + str(s1))