print("Quantos Km você rodou?")
a1 = float (input())
print("Quantos dias você alugou esse carro?")
a2 = int(input())

s1 = int(a2 *60)
s2 = float(a2 * 0.15)

print("Você pagou pelo carro " + str(s1) +  " e pagou pelo Km rodados" + str(s2))