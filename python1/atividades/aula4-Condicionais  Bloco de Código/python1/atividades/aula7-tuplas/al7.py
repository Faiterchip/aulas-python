# DESAFIO 01

# Faça um jogo, onde o computador vai “pensar” em um número
# entre 0 a 10. Só que agora o jogador vai tentar adivinhar até
# acertar, mostrando no final quantos palpites foram necessários
# para vencer.

import random
# # opcoes=[1,2,3,4,5,6,7,8,9,10]
# # pc=random.choice(opcoes)
# pc=random.randint(1,11)
# while True :
#     player=int(input("Digite um numero de 1 a 10: "))
#     if pc==player:
#         print("Você acertou")
#         break
#     else:
#         print("Você errou")
# print(f"voce tentou {player} vezes")

# DESAFIO 02

# Crie um programa que leia vários números inteiros pelo
# teclado. O programa só vai parar quando o usuário digitar o
# valor 999, que é a condição de parada. No final, mostre
# quantos números foram digitados e qual foi a soma entre eles
# (desconsiderando o 999).
# while True:
#     pessoa=int(input("digite o valor correto"))
#     if pessoa==999:
#         print("eee")
#         break
#     resultad=pessoa
# print(f"voce digitou {resultad-1} numeros")




# DESAFIO 03

# Crie um programa que leia vários números inteiros pelo
# teclado. No final da execução, mostre a média entre todos os
# valores e qual foi o maior e o menor valores lidos. O programa
# deve perguntar ao usuário se ele quer ou não continuar a
# digitar valores
# while True:
#     valor=int(input("Digite um numero: "))
#     valor1=int(input("Digite outro numero: "))
#     valor2=int(input("Digite mais um numero: "))
#     valor3=int(input("digite: "))
#     #maior
#     if valor>valor1 and valor>valor2 and valor>valor3:
#         print(f"primeiro e maior= {valor}")
#     elif valor1>valor and valor1>valor2 and valor1>valor3:
#         print(f"segundo e maior= {valor1}")
#     elif valor2>valor and valor2>valor1 and valor2>valor3:
#         print(f"o terceiro e maior= {valor2}")
#     else:
#         print(f"o quarto e maior= {valor3}")
#     #menor
#     if valor<valor1 and valor<valor2 and valor<valor3:
#         print(f"primeiro e menor= {valor}")
#     elif valor1<valor and valor1<valor2 and valor1<valor3:
#         print(f"segundo e menor= {valor1}")
#     elif valor2<valor and valor2<valor1 and valor2<valor3:
#         print(f"o terceiro e menor= {valor2}")
#     else:
#         print(f"o quarto e menor= {valor3}")
#     pessoa=input("quer continuar? (s/n): ")
#     pessoa=pessoa.lower()
#     if pessoa=='n':
#         break
# print("encerrado")

# DESAFIO 04

# Faça um programa que jogue par ou impar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitorias consecutivas que ele conquistou
# no final do jogo.

import random
import time


num_jogador =int(input(">>Escolha um número ente Zero e Dez (0 à 10): "))


print("")
op_jogador =int(input(">>Escolha entre : \n1-IMPAR \n2-PAR \n Digite sua escolha (1 ou 2): "))



num_computador= random.randint(0,11)


print("")
print(f"→Você escolheu: {num_jogador} ")
print(f"→Seu Oponente escolheu: {num_computador} ")


total= num_jogador+num_computador
e_par= total%2==0 #retorna verdadeiro ou falso
    
print("")
print("Vamos contar os dedos!")
print("contando....")
time.sleep(1)
print("contando....")
time.sleep(1)
print("contando....")
time.sleep(1)


print("")
print(f"→Total = {total}")

# DESAFIO 05

# Crie um programa que leia a idade e o sexo de varias
# pessoas. A cada pessoa cadastrada, o programa deverá
# perguntar se o usuário quer ou não continuar. No final, mostre:
# A) Quantas pessoas tem mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres tem menos de 20 anos.
