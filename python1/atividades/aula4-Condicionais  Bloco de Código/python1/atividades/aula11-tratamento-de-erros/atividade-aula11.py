# DESAFIO 01
# Faça um programa que tenha uma função chamada área(), que
# receba as dimensões de um terreno retangular (largura e
# comprimento) e mostre a área do terreno

# def area(largura, comprimento):
#     area_terreno = largura * comprimento
#     return area_terreno
# largura = float(input("Digite a largura do terreno em metros: "))
# comprimento = float(input("Digite o comprimento do terreno em metros: "))
# area_terreno = area(largura, comprimento)
# print(f"A área do terreno é {area_terreno} metros quadrados.")

# DESAFIO 02
# Faça um programa que tenha uma função chamada escreva(), que
# receba um texto qualquer como parâmetro e mostre uma mensagem com
# tamanho adaptável.
# Ex:
# escreva(‘Olá, mundo!!’)
# Saída
# 
# -----------------------------------
# Olá, mundo
# -----------------------------------

# def escreva(texto):
#     tamanho = len(texto)+4  # comprimento do texto + 4 (2 traços de cada lado)
#     print('-'*tamanho)
#     print(f'  {texto}')
#     print('-'*tamanho)
# escreva('paralelepipedo')


# DESAFIO 03
# Faça um programa que tenha uma função chamada maior(), que
# receba três parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é
# o maior.
# a=int(input("1º parametro: "))
# b=int(input("2º parametro: "))
# c=int(input("3º parametro: "))
# def maior(a, b, c):# a é o maior
#     maior_valor = a
#     if b > maior_valor:# Comparando com b
#         maior_valor = b
#     if c > maior_valor:# Comparando com c
#         maior_valor = c 
#     return maior_valor
# resultado = maior(a,b,c)# Retornando o maior valor encontrado
# print(f"O maior valor é: {resultado}")
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
            digt=int(input("digite o primeiro numero para a soma: "))
            digto=int(input("digite o segundo numero para a soma: "))
            print(digt+digto)
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
            digt=int(input("digite o primeiro numero para a subtraçao: "))
            digto=int(input("digite o segundo numero para a subtraçao: "))
            print(digt-digto)
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
        digt=int(input("digite o primeiro numero para multiplicaçao: "))
        digto=int(input("digite o segundo numero para multiplicaçao: "))
        print(f"tabuada do {digt}: ")
        for i in range(1,digto+1):
            print(f"{digt} X {i} = {digt*i}")
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
                digt=float(input("digite o primeiro numero para a divisao: "))
                digto=float(input("digite o segundo numero para a divisao: "))
                print(digt/digto)
        n=input("digite (0) para sair, aperte (enter) para continuar: ")
        if n=="0":
            print("saindo...")
            time.sleep(1)
            break

print("bem vindo a calculadora")
time.sleep(2)
while True:
    print("------------------------------------------------------------")
    digct=int(input("digite a operaçao que deseja fazer (1=soma),(2=subtraçao),(3=multiplicaçao),(4=divisao): "))
    print("------------------------------------------------------------")
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
