a = [0,0,0,0]
cont = int(0)
s1 = int(0)

for k in a:
    print("Digite um número")
    a[k]= int(input())
    if(a[k] == 9):
        s1 = s1 +1

print(f"O número 9 aparece {s1} vezes")