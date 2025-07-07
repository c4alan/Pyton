import Ex112funcoes

print("Qual o seu cargo?")
a = str(input())

t = Ex112funcoes.analisar(a)
s1 = int(t * 12)

print(f"Seu salário é R${t} e sua renda anul é R${s1}")