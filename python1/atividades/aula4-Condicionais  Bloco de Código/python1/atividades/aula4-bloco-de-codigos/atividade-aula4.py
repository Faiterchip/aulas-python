# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que
# ele foi multado.
# A multa vai custar R$ 7,00 por cada Km acima do limite.

# vol=int(input("Digite sua velocidade (km/h) "))
# if vol>80:
#     print(f"tu foi multado! sua multa foi de {(vol-80)*7} reais")
# else:
#     print("passar bem")
# print("fim")

# Desenvolva um programa que pergunte a distância de uma
# viagem em Km. Calcule o preço da passagem cobrando R$
# 0,50 por Km para viagens de até 200 Km e R$ 0,45 para
# viagens mais longas.

# km=int(input("quantos (km/h) voce vai viajar? "))
# if km<=200:
#     print(f"O valor da sua viagem é: {km*0.50}")
# else:
#     print(f"O valor da sua viagem é: {km*0.45}")
    
# Faça um programa que leia três números e mostre qual é o
# maior e qual é o menor.

# num1=int(input("Digite um numero: "))
# num2=int(input("Digite outro numero: "))
# num3=int(input("Digite mais um numero: "))

# Escreva um programa que faça o computador “pensar” em um
# número inteiro entre 5 e 0 e peça para o usuário tentar descobrir
# qual foi o número escolhido pelo computador.

# O programa deverá escrever na tela se o usuário venceu ou
# perdeu.

# import random
# print("jogo do adivinhe o numero")
# numero=int(input("digite um numero entre 0 e 10: "))
# numerocomputador=random.randint(0,10)
# if numero==numerocomputador:
#     print("acertou")
# else:
#     print("errou")
    
# Media escola
# Aprovado se  media maior ou igual a 7
# faltas até 10
# media=5
# faltas=9
# if media>=7 and faltas<=10:
#     print("passsou")
# else:
#     if media<3:
#         print("reprovado")
#     else:
#         print("recuperaçao")
        
# if media>=7 and faltas<=10:
#     print("passsou")
# elif media<3:
#     print("reprovado")
# else:
#     print("recuperaçao")

# if media<7:
#     print("reprovado")
# elif faltas>10:
#     print("reprovado")
# else:
#     print("aprovado")

# DESAFIO 04

# Faça um programa que leia três números e mostre qual é o
# maior e qual é o menor.

# valor=int(input("Digite um numero: "))
# valor1=int(input("Digite outro numero: "))
# valor2=int(input("Digite mais um numero: "))
# #maior
# if valor>valor1 and valor>valor2:
#     print(f"primeiro e maior= {valor}")
# elif valor1>valor and valor1>valor2:
#     print(f"segundo e maior= {valor1}")
# else:
#     print(f"terceiro e maior= {valor2}")
# #menor
# if valor<valor1 and valor<valor2:
#     print(f"primeiro e menor= {valor}")
# elif valor1<valor and valor1<valor2:
#     print(f"segundo e menor= {valor1}")
# else:
#     print(f"terceiro e menor= {valor2}")
    
# DESAFIO 05

# Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo.
# Condições Necessárias:🙌🙌🙌👍
# a + b > c
# a + c > b
# b + c > a

# a=int(input("digite uma reta A: "))
# b=int(input("digite uma reta B: "))
# c=int(input("digite uma reta C: "))

# if (a+b>c) and (b+c>b) and (a+c>b):
#     print(f"e um triangulo👍")
# else:
#     print("nao e um triangulo🤔")
    
# DESAFIO 01

# Escreva um programa para aprovar um empréstimo bancário
# para a compra de uma casa. O programa vai perguntar o valor
# da casa, o salário do comprador e em quantos anos ele vai
# pagar.

# Calcule o valor da prestação mensal, sabendo que ela não pode
# exceder 30% do salário ou então o empréstimo será negado.

# valor_casa=float(input("digite o valor da casa  "))
# salario=float(input("digite seu salario  "))
# anos_pagar=int(input("quantos anos pretende pagar  "))
# meses=anos_pagar*12
# prestacao=valor_casa/meses
# print(f"meses a pagar = {meses}")
# print(f"valor da prestacao = {prestacao}")
# porcentagem=salario*0.30
# if porcentagem>prestacao:
#     print("compra negada")
# else:
#     print("compra permitida")

# DESAFIO 02
# Escreva um programa que leia dois números inteiros e
# compare- os, mostrando na tela uma mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais
    
valor=int(input("Digite um numero: "))
valor1=int(input("Digite outro numero: "))
#maior
if valor>valor1:
    print(f"O primeiro e maior= {valor}")
elif valor==valor1:
    print("Não existe valor maior, os dois são iguais")
    
else:
    print(f"O segundo e maior= {valor1}")
    
# DESAFIO 03

# Crie um programa que leia duas notas entre 0 a 10 de um aluno
# e calcule sua média, mostrando uma mensagem no final, de
# acordo com a média atingida.
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 a 6.9: RECUPERAÇÃO
# Média igual ou superior a 7.0: APROVADO

# media=float(input("Digite sua media (0 a 10): "))
# media1=float(input("Digite sua outra media (0 a 10): "))
# result=media+media1
# nota=result/2
# if nota<5.0:
#     print("reprovado")
# elif nota<6.9:
#     print("recuperaçao")
# else:
#     print("aprovado")

# DESAFIO 04

# A confederação Nacional de Natação precisa de uma programa
# que leia o ano de nascimento de uma atleta e mostre sua
# categoria, de acordo com a idade.
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JUNIOR
# Até 24 anos: SÊNIOR
# Acima: MASTER

# from datetime import datetime
# anoAtual=datetime.now().year
# print(anoAtual)

# idade=int(input("digite sua idade"))
# if idade<9:
#     print("nao pode participar")
# elif idade<14:
#     print("bem vindo mirim")
# elif idade<19:
#     print("bem vindo infantil")
# elif idade<24:
#     print("bem vindo junior")
# elif idade>24:
#     print("bem vindo master")
    
# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso
# de mostrar que tipo de triângulo será formado:
# Equilátero: Todos os lados iguais
# Isósceles: Dois lados iguais
# Escaleno: Todos os lados diferentes



# DESAFIO 06

# Crie um programa que faça o computador jogar Jokenpô com
# você:

import random #importar random antes de usar o random
usuario=int(input("digite sua escolha (1-pedra,2-papel ou 3-tesoura):  "))
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
    print("****************voce venceu*********************")
elif ((tx_jogador=="TESOURA" and pc_ramdomico=="PEDRA") or
    (tx_jogador=="PAPEL" and pc_ramdomico=="TESOURA") or
    (tx_jogador=="PEDRA" and pc_ramdomico=="PAPEL")   
) :
    print("*******************voce perdeu**************")
else:
    print("**************empate****************")
print(f"voce jogou {tx_jogador}")
print(f"a maquina jogou {pc_ramdomico}")