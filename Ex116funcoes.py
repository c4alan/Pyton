def investigar(a,a1,a2,a3,a4):
    s1 = int(0)
    s2 = str("")
    if(a == "sim"):
        s1 = s1 + 1
    if(a1 == "sim"):
        s1 = s1 + 1
    if(a2 == "sim"):
        s1 = s1 + 1
    if(a3 == "sim"):
        s1 = s1 + 1
    if(a4 == "sim"):
        s1 = s1 +1
    if(s1 == 2):
        s2 = ("Suspeito")
    elif(s1 >2 and s1 <=4):
        s2 = ("Cúmplice")
    elif(s1 > 4):
        s2 = ("Assassino")
    elif(s1 <2):
        s2 = ("inocente")
    return s2