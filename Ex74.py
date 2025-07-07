s1 = int(0)
for cont in range(0,3,1):
    print("Digite um nome")
    a = str(input())
    print("Digite o genêro")
    a1 = str(input())
    if(a1 == "Homem" or a1 == "Masculino"):
        s1 = s1 +1

print(f"{s1} homens foram cadastrados")