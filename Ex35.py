print("Qual o valor da casa?")
a1 = float(input())
print("Qual o seu salário?")
a2 = float(input())
print("Quantos meses vai pagar?")
a3 = int(input())

s1 = float(a1 / a3)

if(s1 > a2 * 0.3):
    print("Empréstimo negado")