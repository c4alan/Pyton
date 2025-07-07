c = int(0)
s1 = int(0)
s2 = int(0)

while(c < 3):
    print("Digite o nome")
    a = str(input())
    print("Digite a idade")
    a1 = int(input())
    if(a == "João" and a1 > 35):
        print("Permissão concedida!")
        break
    if(c > 3):
        print("Bloqueado")
        break
    if(a != "João"):
        s1 = s1 +1
    if(a1 < 35):
        s2 = s1 + 1
    c = c +1
print(f"Você errou o nome {s1} vezes e errou a idade {s2} vezes")