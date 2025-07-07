c= int(0)
s1 = int(0)
s2 =int(0)

while (c<999):
    print("Digite um número")
    a1 = int(input())
    if(a1 > 0):
        s1 = s1 + 1
        s2 = s2 + a1
    c= c +1

print(f"Foram feitas {s1} tentativas \nA soma dos números digitados é {s2}")