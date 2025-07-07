c = int(0)
s1 = int(0)
s2 = int(9999999999999999999)
s3 = str("")
s4 = str("")

while (c <5):
    c = c +1
    print("Digite um nome")
    a1 = str(input())
    print("Digite o genêro")
    a2 = str(input())
    print("Digite a idade")
    a3 = int(input())
    if(a3 > s1 and a2 == "masculino"):
        s1 = a3
        s3 = a1
    if(a3 < s2 and a2 == "feminino"):
        s2 = a3
        s4 = a1

print(f"O homem mais velho com nome de {s3} tem {s1} anos e a mulher mais jovem tem o nome de {s4} e tem {s2} anos")