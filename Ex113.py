import Ex113funcoes
import random

a = [random.randint(0,10),random.randint(0,10),random.randint(0,10),random.randint(0,10)]

print(a)

t =  Ex113funcoes.analisar(a)
t1 = Ex113funcoes.analisa2(a)
s1 = int(t + t1 * 3.14)
print(f"O dobro do terceiro sorteio é {t}\nO triplo do segundo sorteio é {t1}\nE a soma dos valores vezes P.I é {s1}")