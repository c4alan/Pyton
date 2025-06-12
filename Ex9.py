print("Qual o preço do produto adquirido?")
a1 = float(input())
print("Qual o desconto?")
a2 = float(input())
s1 = float(a1 - a1 * (a2/100))

print ("O produto custva " + str(a1) + " mas teve desconto de " + str(a2) + "% por isso agora está custando " + str(s1) + " reais")