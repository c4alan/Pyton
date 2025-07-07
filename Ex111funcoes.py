def maioremenor(a,a1):
    s1 = int(0)
    s2 = int(9999999999)
    if(a > s1):
        s1 = a
    if(a1 > s1):
        s1 = a1
    if(a < s2):
        s2 = a
    if(a1 < s2):
        s2 = a1
    s3 = int(0)
    s3 = (s1 + s2) /2
    return s1,s2,s3