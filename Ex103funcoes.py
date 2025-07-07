def analisar(a,a1,a2):
    s1 = int(0)
    s2 = int(99999)
    if(a > s1):
        s1 = a

    if(a1 > s1):
        s1 = a1

    if(a2 > s1):
        s1  = a2
    if(a < s2):
        s2 = a
    if(a1 < s2):
        s2 = a1
    if(a2 < s2):
        s2 = a2
    print(f"O maior número é {s1} e o  menor é {s2}")