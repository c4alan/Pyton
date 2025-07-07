import Ex10funcoes

print("Qual o seu peso?")
a = float(input())
print("Escolha um planeta para ver seu peso:\n[1]Mercurio\n[2]Venus\n[3]Marte\n[4]Jupiter\n[5]Saturno\n[6]Urano")
b = int(input())
match b:
    case 1:
        Ex10funcoes.mercurio(a,b)
    case 2:
        Ex10funcoes.venus(a,b)
    case 3:
        Ex10funcoes.marte(a,b)
    case 4:
        Ex10funcoes.jupiter(a,b)
    case 5:
        Ex10funcoes.saturno(a,b)
    case 6:
        Ex10funcoes.urano(a,b)