import Ex107funcoes

print("Você possui alguma dívida?")
a = str(input())

if(a == "Não" or a == "não"):
    print("Continue assim!")
else:
    print("Qual a sua dívida?")
    a1 = float(input())
    print("Qual o tempo da sua dívida?")
    a2 = int(input())
    print("Qual taxa dos juros?")
    a3 = float(input())
    Ex107funcoes.lascado(a1,a2,a3)