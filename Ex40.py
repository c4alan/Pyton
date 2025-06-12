print("Quantos aulas você deu esse mês?")
a1 = int(input())

s1 = float(a1 * 40.0)

if(s1 == 1518):
    s2= a1
    print("Seu salario final é " + str(s2))

if(s1 > 1518 and s1 < 2793.88):
    s3 = float(a1 - a1 * 0.09)
    print("Seu salario final é " + str(s3))

if(s1 > 2793.88 and s1 < 4190.83):
    s4 = a1 - a1 * 0.12
    print("Seu salario final é " + str(s4))

if(s1 > 4190.83 and s1 < 8157.41):
    s5 = a1 - a1 * 0.14
    print("Seu salario final é " + str(s5))