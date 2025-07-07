j = float(1.50)
s = float(1.1)
c = int(0)

while (s < j):
    s = float(s + 0.03)
    j = float(j + 0.02)
    print(f"{j} e {s}")
    if (s < j):
        c = c + 1
print(f"Demorou {c} anos para Sara ser maior do que francisco")
    