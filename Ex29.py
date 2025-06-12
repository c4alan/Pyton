print("Digite a 1ª idade")
a1 = int(input())
print("Digite a 2ª idade")
a2 = int(input())
print("Digite a 3ª idade")
a3 = int(input())
print("Digite a 4ª idade")
a4 = int(input())

s1 = int(0)
s2 = int(9999999)

if(a1 > s1):
    s1 = a1
if(a1 < s2):
    s2 = a1
if(a2 > s1):
    s1 = a2
if(a2 < s2):
    s2 = s2
if(a3 > s1):
    s1 = a3
if(a3 < s2):
    s2 = a3
if(a4 > s1):
    s1 = a4
if(a4 < s2):
    s2 = a4

print("O mais jovem tem " + str(s2) + " anos e o mais velho tem " + str(s1) + " anos")