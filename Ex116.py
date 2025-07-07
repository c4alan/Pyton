import Ex116funcoes

print("Telefonou para a vítima?")
a = str(input())
print("Esteve no local do crime?")
a1 = str(input())
print("Mora perto da vítima?")
a2= str(input())
print("Devia para a vítima?")
a3 = str(input())
print("Já trabalhou com a vítima?")
a4 = str(input())

t = Ex116funcoes.investigar(a,a1,a2,a3,a4)
print(f"Você foi considerado {t}")
