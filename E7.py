a = []
b = []

for cont in range(3):
    print("Digite um nome")
    a.append(str(input()))
    print("Digite o salário")
    b.append(float(input()))

print(f"Foram cadastrados os seguintes nomes:\n{a}\nForam cadastrados os seguintes salários:\n{b}")