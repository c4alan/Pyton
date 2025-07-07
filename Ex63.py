c = str("")
s1 = int(1)
while(c != "sim"):
    print("Digite o usuário")
    a1 = str(input())
    print("Digite a senha")
    a2= str(input())
    if(a1 == "fácil" and a2 =="ff"):
        print("Acesso concedido")
        break
    else:
        
        if(c != "sim"):
            s1 = s1 *2
            print(f"Senha ou usuario incorreto multa de R${s1}")
            print("deseja parar?")
            c = input()
            if(c == "sim"):
                print(f"Sua multa final é R${s1}")
                break
            
      
    