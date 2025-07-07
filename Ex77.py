s1= int(0)
s2= int(0)
s3 = int(0)

for cont in range(0,4,1):
    print("Cadastre um nome")
    a1 = str(input())
    print("Cadastre a idade")
    a2 = int(input())
    print("Cadastre o sexo")
    a3 = str(input())
    if(a2 > 10):
        s1 = s1 +1
    if(a3 == "masculino" or a3 == "Masculino"):
        s2 = s2 +1
    if(a3 == "Feminino" or a3 == "feminino" and a2 <20):
        s3 = s3 + 1
print(f"Existem {s1} pessoas com menos de 10 anos\nExistem {s2} homens\nExistem {s3} mulheres com menos de 20")