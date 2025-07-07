import random
s1 = int(0)
a= [random.randint(0,10),random.randint(0,10),random.randint(0,10),random.randint(0,10)]

print("Digite um número")
a1 = int(input())

for k in a:
    print(f"Foram sorteados {k}")
    if(a1 == k):
        a1 = a1 + k

print(f"A soma do número escolhido é {a1}")