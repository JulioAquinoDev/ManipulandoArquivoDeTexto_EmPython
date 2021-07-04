import os
from time import sleep

a = open("Cadastro.txt","a+")

while True:
    print("="*30)
    print("Sistema de Cadastro".center(30))
    print("="*30)
    print("(1) - Novo Cadastro")
    print("(2) - Ver Cadastro")
    print("(3) - Buscar")
    print("(4) - Sair")
    print("-"*30)
    op = input("Qual sua opçao: ")
    os.system("cls")
    
    if op =="1":
        a = open("Cadastro.txt","a")
        print("="*30)
        print("Novo Cadastro".center(30))
        print("="*30)
        nome = str(input("Nome: "))
        rg = int(input("CPF: "))
        idd = int(input("Idade: "))
        tel = str(input("Nº Tel: "))
        cidade = str(input("Cidade: "))
        a.write(f"{nome}, {rg}, {idd} anos, {tel}, {cidade}.\n")
        a.close()
        os.system("cls")
        print("="*30)
        print("Cadastro Realizado".center(30))
        print("="*30)
        print(f"{nome} foi cadastrado com sucesso!")
        print("-"*30)
        sleep(2)
        os.system("cls")
        
    elif op =="2":
        a = open("Cadastro.txt","r")
        print("="*30)
        print("Cadastros Realizados.".center(30))
        print("="*30)
        print(a.read())
        print("-"*30)
        print("(1) - Voltar")
        print("(2) - Sair")
        print("-"*30)
        cont = input("Digite uma tecla para voltar: ")
        os.system("cls")

        if cont =="1":
            True
            
        elif cont =="2":
            False
            break
        else:
            print("="*30)
            print("Erro.".center(30))
            print("="*30)
            print("Opção inválida.")
            print("-"*30)
            sleep(1)
            os.system("cls")
            
            

    elif op =="3":
        a = open("Cadastro.txt","r")
        print("="*30)
        print("Busca de Cadastro".center(30))
        print("="*30)
        busca = str(input("Digite o nome: "))
        os.system("cls")
        for i in a:
            if busca in i:
                print("="*30)
                print("Busca de Cadastro".center(30))
                print("="*30)
                print(i)
                print("-"*30)
                print("(1) - Voltar")
                cont = input("Digite a opção para voltar: ")
                os.system("cls")

                if cont == "1":
                    True
                    
                else:
                    print("="*30)
                    print("Erro.".center(30))
                    print("="*30)
                    print("Opção inválida.")
                    print("-"*30)
                    sleep(1)
                    os.system("cls")
        
    elif op =="4":
        print("="*30)
        print("Saindo...".center(30))
        print("="*30)
        sleep(1)
        break

    else:
        print("="*30)
        print("Erro.".center(30))
        print("="*30)
        print("Opção inválida.")
        print("Tente novamente.")
        print("-"*30)
        sleep(1)
        os.system("cls")
