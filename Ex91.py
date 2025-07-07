a = [3,0,0,0,0,0,0,0,0,0]
cont = int(0)
for cont in range(0,10,1):
    a[cont + 1]= a[cont]*2
    print(a[cont])
    if(a[cont] == 3 or a[cont] == 6 or a[cont] == 96):
        print(f"${a[cont]}$")
    else:
        print(a[cont])