def analisar(a):
    s1 = int(0)
    if(a == "policial" or a == "médico"):
        s1 = 2000
    elif(a == "mágico" or a == "coach"):
        s1 =1500
    else:
        s1 = 500
    return s1