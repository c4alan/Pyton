print("Tem 1000 ou mais cc?")
a1 = str(input())
print("É a rainha do corte de giro?")
a2 = str(input())
print("É uma big trail?")
a3 = str(input())
print("Pega altas velocidades?")
a4 = str(input())
print("Estilo naked, esportivo ou trail?")
a5 = str(input())

s1 = int(0) #xj6
s2 = int(0) #s1000 rr
s3 = int(0) #triumph tiger 900
s4 = int(0) #cbr 1100/ Africa twin
s5 = int(0) #tiger sport 660

if(a1 == "sim"):
    s2 = s1 + 1
    s4 = s4 + 1
else:
    s1 = s1 + 1
    s3 = s3 + 1
    s5 = s5 + 1
if(a2== "sim"):
    s1 = s1 + 1
    s2 = s2 + 1
else:
    s3 = s3 + 1
    s4 = s4 + 1
    s5 = s5 + 1
if(a3 == "sim"):
    s3 = s3 + 1
    s4 = s4 + 1
else:
    s1 = s1 + 1
    s2 = s2 + 1
    s5 = s5 + 1
if(a4 == "sim"):
    s1 = s1 + 1
    s2 = s2 + 1
    s3 = s3 + 1
    s4 = s4 + 1
    s5 = s5 + 1
if(a5 == "naked"):
    s1 = s1 +1
elif(a5 == "trail"):
    s3 = s3 + 1
    s4 = s4 + 1
else:
    s2 = s2 + 1
    s5 = s5 + 1

print("XJ6 tem " + str(s1) + " pontos")
print("BMW S1000RR tem " + str(s2) + " pontos")
print("Triumph tiger 900 Rallypro tem " + str(s3) + " pontos")
print("CBR 1100 Africa Twin tem " + str(s4) + " pontos")
print("Tiger Sport 660 tem " + str(s5) + " pontos")