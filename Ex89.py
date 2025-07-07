c = int(0)

for cont in range(0,3,1):
    print("Digite um nome")
    a = str(input())
    print("Digite seu sexo")
    b = str(input())
    if(b == "masculino" or b == "Masculino"):
        c = c + 1
print(f"Existem {c} homens cadastrados")