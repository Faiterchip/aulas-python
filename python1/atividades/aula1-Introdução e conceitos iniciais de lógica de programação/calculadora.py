import time
def soma():
    while True:
        print("----------------------------------------------")
        print("1 = soma escolhido")
        time.sleep(1)
        digg=input("quer que seja em formato de tabuada? (s/n): ")
        if digg=="s":
            digto=int(input("digite o numero para a soma: "))
            ding=int(input("ate onde vai a tabuada: "))
            for i in range(1,ding+1):
                print(f"{i} + {digto} = {i+digto}")
        else:
            try:
                digt=int(input("digite o primeiro numero para a soma: "))
                digto=int(input("digite o segundo numero para a soma: "))
                print(digt+digto)
            except Exception as a:
                print(f"ocorreu um erro inesperado")
                time.sleep(2)
                print("provavelmente foi culpa sua")
                time.sleep(1)
                print("tentando novamente")
                time.sleep(1)
                break
        n=input("digite (0) para sair, aperte (enter) para continuar: ")
        if n=="0":
            print("saindo...")
            time.sleep(1)
            break
def subtracao():
    while True:
        print("2 = subtraçao escolhido")
        time.sleep(1)
        digg=input("quer que seja em formato de tabuada? (s/n): ")
        if digg=="s":
            digto=int(input("digite o numero para a soma: "))
            ding=int(input("ate onde vai a tabuada: "))
            for i in range(1,ding+1):
                print(f"{i} - {digto} = {i-digto}")
        else:
            try:
                digt=int(input("digite o primeiro numero para a subtraçao: "))
                digto=int(input("digite o segundo numero para a subtraçao: "))
                print(digt-digto)
            except Exception as a:
                print(f"ocorreu um erro inesperado")
                time.sleep(2)
                print("provavelmente foi culpa sua")
                time.sleep(1)
                print("tentando novamente")
                time.sleep(1)
                break
        n=input("digite (0) para sair, aperte (enter) para continuar: ")
        if n=="0":
            print("saindo...")
            time.sleep(1)
            break
def multiplicacao():
    while True:
        print("----------------------------------------------")
        print("3 = multiplicaçao escolhido")
        time.sleep(1)
        digg=input("quer que seja em formato de tabuada? (s/n): ")
        if digg=="s":
            digt=int(input("digite o primeiro numero para multiplicaçao: "))
            digto=int(input("ate aonde vai a tabuada: "))
            print(f"tabuada do {digt}: ")
            for i in range(1,digto+1):
                print(f"{digt} X {i} = {digt*i}")
        else:
            try:
                digt=int(input("digite o primeiro numero para a multiplicaçao: "))
                digto=int(input("digite o segundo numero para a multiplicaçao: "))
            except Exception as a:
                print(f"ocorreu um erro inesperado")
                time.sleep(2)
                print("provavelmente foi culpa sua")
                time.sleep(1)
                print("tentando novamente")
                time.sleep(1)
                break
            print(f"{digt} X {digto} = {digt*digto}")
        n=input("digite (0) para sair, aperte (enter) para continuar: ")
        if n=="0":
            print("saindo...")
            time.sleep(1)
            break
def divisao():
    while True:
        print("----------------------------------------------")
        print("4 = divisao escolhido")
        time.sleep(1)
        digg=input("quer que seja em formato de tabuada? (s/n): ")
        if digg=="s":
            digto=int(input("digite o numero para a divisao: "))
            ding=int(input("ate onde vai a tabuada: "))
            for i in range(1,ding+1):
                print(f"{i} + {digto} = {i/digto}")
        else:
            try:    
                digt=float(input("digite o primeiro numero para a divisao: "))
                digto=float(input("digite o segundo numero para a divisao: "))
                print(digt/digto)
            except Exception as a:
                print(f"ocorreu um erro inesperado")
                time.sleep(2)
                print("provavelmente foi culpa sua")
                time.sleep(1)
                print("tentando novamente")
                time.sleep(1)
                break
        n=input("digite (0) para sair, aperte (enter) para continuar: ")
        if n=="0":
            print("saindo...")
            time.sleep(1)
            break
print("bem vindo a calculadora")
time.sleep(2)
print("aonde voce pode calcular altas coisas")
time.sleep(1)
while True:
    try:
        print("-----------------------------------------------------------------------------------------------")
        digct=int(input("digite a operaçao que deseja fazer (1=soma),(2=subtraçao),(3=multiplicaçao),(4=divisao): "))
        print("-----------------------------------------------------------------------------------------------")
    except Exception as a:
        print(f"serio????")
        time.sleep(2)
        print("voce nao consegue seguir instruçoes simples????")
        time.sleep(1)
        print("tentando novamente")
        time.sleep(1)
        continue
    if digct==1:
        soma()
    elif digct==2:
        subtracao()
    elif digct==3:
       multiplicacao()
    elif digct==4:
           divisao()
    else:
        print("escolha invalida")