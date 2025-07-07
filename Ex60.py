c = str("")
s1 = int(0)
s2 = int(0)
s3 = int(0)
s4 = int(0)

while (c != "Sim"):
    print("Digite um número")
    a1 = int(input())
    print("Deseja parar?")
    c = input()
    if(a1 < 0):
        s1 = s1 + 1
    if(a1 > 0):
        s2 = s2 + 1
        s3 = s3 + a1
        s4 = s3/s2

print(f"Existem {s1} números negativos\nExitem {s2} números positivos e a média deles é {s4}")

