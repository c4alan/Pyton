import Ex117funcoes

print("escolha uma promoção:\n[1]Álcool até 20 litros, desconto de 3% por litro, acima de 20 litros desconto de 5% por litro\n[2]Gasolina até 20 litros, desconto de 4% por litro, acima de 20 litros, desconto de 6% por litro")
a = int(input())

match a:
    case 1:
        print("Quantos litros você abasteceu?")
        b = int(input())
        t = Ex117funcoes.alcool(a,b)
        print(f"O total ficou em R${t}")
    case 2:
        print("Quantos litros você abasteceu?")
        b = int(input())
        t = Ex117funcoes.gas(a,b)
        print(f"O total ficou em R${t}")
