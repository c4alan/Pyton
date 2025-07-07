import random
a = ["Pedra","Papel","Tesoura","Spock","Lagarto"]
a1 = random.randint(0,4)

print("Escolha:\n[1]Papel\n[2]Pedra\n[3]Tesoura\n[4]Lagarto\n[5]Spock")
a2 = int(input())
print(f"Foi sorteado {a[a1]}")
match a2:
    case 1:
        if(a[a1] == "Papel"):
            print("Empatou")
        if(a[a1] == "Tesoura"):
            print("Perdeu!")
        if(a[a1] == "Lagarto"):
            print("Perdeu!")
        if(a[a1] == "Pedra"):
            print("Ganou!")
        if(a[a1] == "Spock"):
            print("Ganhou!")
    case 2:
        if(a[a1] == "Pedra"):
            print("Empate")
        if(a[a1] == "Papel"):
            print("Perdeu!")
        if(a[a1] == "Spock"):
            print("Perdeu!")
        if(a[a1] == "Tesoura"):
            print("Ganhou!")
        if(a[a1] == "Lagarto"):
            print("Ganhou!")
    case 3:
        if(a[a1] == "Tesoura"):
            print("Empate")
        if(a[a1] == "Pedra"):
            print("Perdeu!")
            if(a[a1] == "Spock"):
                print("Perdeu!")
        if(a[a1] == "Papel"):
            print("Ganhou!")
        if(a[a1] == "Lagarto"):
            print("Ganhou!")
    case 4:
        if(a[a1] == "Lagarto"):
            print("Empate")
        if(a[a1] == "Tesoura"):
            print("Perdeu")
        if(a[a1] == "Pedra"):
            print("Perdeu!")
        if(a[a1] == "Papel"):
            print("Ganhou!")
        if(a[a1] == "Spock"):
            print("Ganhou!")
    case 5:
        if(a[a1] == "Spock"):
            print("Empate")
        if(a[a1] == "Lagarto"):
            print("Perdeu!")
        if(a[a1] == "Papel"):
            print("Perdeu!")
        if(a[a1] == "Tesoura"):
            print("Ganhou!")
        if(a[a1]=="Pedra"):
            print("Ganhou!")

