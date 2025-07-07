s1 = int(0)
s2 = int(0)
s3 = int(0)
s4 = int(0)
s5 = int(0)


for cont in range(0,4,1):
    print("Digite um número")
    a = int(input())
    if(a %2 == 0):
        s1 = s1 + 1
        s2 = s2 + a
    if(a %2 == 1):
        s3 = s3 + 1
        s4 = s4 + a
s5 = s2 + s4
print(f"Foram cadastrados {s1} números pares\nForam cadastrados {s3} números ímpares\nA soma dos pares é {s2}\nA soma dos ímpares é {s4}\nA soma geral é {s5}")