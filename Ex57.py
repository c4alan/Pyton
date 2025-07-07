print("O peso médio do brasileiro é 69 Kg")

c = int(0)
s1 = int(0)
s2 = int(0)

while(c < 4):
    c = c +1
    print("Digite seu peso")
    a1 = float(input())
    if(a1 <= 69):
        s1 = s1 + 1
    if(a1 > 69):
        s2 = s2 + 1

print(f"Exite {s1} pessoas que estão igual ou abaixo do médio \nExites {s2} que estão acima do peso médio")