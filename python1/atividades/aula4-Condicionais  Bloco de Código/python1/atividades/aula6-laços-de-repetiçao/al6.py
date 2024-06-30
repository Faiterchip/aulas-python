# for contador in range(1,7): #contador = contador+1
#     print(contador)#1
#     input()
    
# for contado in range(1,7,2):#pula 1
#     print(contado)
# numero=int(input("digite um numero: "))
# for i in range(0,61):
#     print(f"{numero} X {i}= {numero*i}")
# print("fim")
    
# numero=int(input("digite um numero: "))
# for i in range(0,100):
#     print(f"{numero} - {i}= {numero-i}")
# print("fim")
    
# numero=int(input("digite um numero: "))
# for i in range(0,601):
#     print(f"{numero} + {i}= {numero+i}")
# print("fim")


# inicio=int(input("digite o primeiro numero: "))
# fim=int(input("digite o fim: ")) #quantidade de repetiçao
# salto=int(input("digite o salto: ")) #pulagems
# texto="calculo :"
# soma=0
# for i in range(inicio,fim,salto): #numero = 3
#     soma=soma+i #soma=3+3
#     print(soma)#1,3,6
#     texto= texto+str(i)
#     if i>50:
#         texto=texto+"\npassou de 50"
#         break   #para o codigo quando for true
#     if i != fim-1:
#         texto=texto+"+"
# print(texto)
# print(f"soma = {soma}")

# nome="jundiapeba"
# for i in nome:
#     print(i)
# lista=[1,23,56,6]
# zoo=["zebra",15,"canguru",98,"gorila",1,"javali",20,"hiena",55]
# for animal in zoo:
#     print(animal)
    
# numero=[1,2,3,10,12]
# for i in numero:
#     if i==10:
#         break
#     print(f"numero={i}")
# else:
#     print("acabou")
# print("fim")
    
# for x in [1,10,20,30,40,50]: #começo👈
#     if x==30:
#         continue #ignora a proxima açao quando for true e ja vai para o começo
#     print(x)
x=1
while x<10:
    print(x)
    x+=1 #mesma coisa de x=x+1
else:
    print("acabou")
    
while True:

    import random #importar random antes de usar o random
    usuario=int(input("digite sua escolha \n1-pedra\n2-papel\n3-tesoura:  "))
    if usuario==1:
        tx_jogador="pedra"
    if usuario==2:
        tx_jogador="papel"
    if usuario==3:
        tx_jogador="tesoura"
    tx_jogador=tx_jogador.upper()
        
    opcoes=["PEDRA","PAPEL","TESOURA"] #as opçoes da maquina
    # pc_ramdomico=random.randint(0.2)
    # print(opcoes)#random.radiant(0.2)
    # print(opcoes[1])#papel
    pc_ramdomico=random.choice(opcoes)
    if ((tx_jogador=="PEDRA" and pc_ramdomico=="TESOURA") or
        (tx_jogador=="TESOURA" and pc_ramdomico=="PAPEL") or
        (tx_jogador=="PAPEL" and pc_ramdomico=="PEDRA")   
    ) :
        print("😎voce venceu---------------------------------voce venceu😎")
    elif ((tx_jogador=="TESOURA" and pc_ramdomico=="PEDRA") or
        (tx_jogador=="PAPEL" and pc_ramdomico=="TESOURA") or
        (tx_jogador=="PEDRA" and pc_ramdomico=="PAPEL")   
    ) :
        print("🤔voce perdeu----------------------------voce perdeu😥")
    else:
        print("😐empate---------------------------------empate😑")
    print(f"voce jogou {tx_jogador}")
    print(f"a maquina jogou {pc_ramdomico}")
    print("------------------------------------")
    resposta=input("deseja sair s/n: ")
    if resposta.lower() == 's':
        print("encerrando")
        break
    print("continuando")