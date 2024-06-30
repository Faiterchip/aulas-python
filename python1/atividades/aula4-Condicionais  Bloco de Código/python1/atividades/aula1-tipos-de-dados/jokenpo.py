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