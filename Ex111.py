import Ex111funcoes
  
print("Digite um número")
a = int(input())
print("Digite outro número")
a1 = int(input())

t = Ex111funcoes.maioremenor(a,a1)
print(f"O maior número é {t[0]} e o menor é {t[1]}")
print(f"E a média é {t[2]}")
