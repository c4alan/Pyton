c = int(0)
soma = int(0)

while (c < 500):
    c = c + 1
    if(c %5 == 0 and c %2 ==1):
        soma = soma + c
        print(f"{c}")
print(f"{soma}")