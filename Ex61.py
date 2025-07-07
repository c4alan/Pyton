c = str("")
s1 = int(0)
s2 = int(0)
s3 = int(0)
s4 = int(0)

while (c != "Sim"):
    print("Digite um número")
    a1 = int(input())
    print("Quer parar?")
    c = input()
    

    if(a1 >= 0 and a1 <= 25):
        s1 = s1 +1
    if(a1 > 25 and a1 <= 50):
        s2 = s2 +1
    if(a1 > 50 and a1 <= 75):
        s3 = s3 + 1
    if(a1 > 75 and a1 <= 100):
        s4 = s4 +1

print(f"Existem {s1} números entre 0 e 25 \nExsitem {s2} números entre 26 e 50 \nExitem {s3} números entre 51 e 75\nExitem {s4} números entre 76 e 100 \nNessa tabela")