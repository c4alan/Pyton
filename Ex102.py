import Ex102funcoes

print("Digite um número")
a = int(input())
print("Digite outro número")
b = int(input())

print("Escolha uma operação:\n[1]Soma\n[2]Subtração\n[3]Multiplicaçã\n[4]Divisão")
c = int(input())

match c:
    case 1:
        Ex102funcoes.soma(a,b)
    case 2:
        Ex102funcoes.subtracao(a,b)
    case 3:
        Ex102funcoes.multi(a,b)
    case 4:
        Ex102funcoes.divi(a,b)