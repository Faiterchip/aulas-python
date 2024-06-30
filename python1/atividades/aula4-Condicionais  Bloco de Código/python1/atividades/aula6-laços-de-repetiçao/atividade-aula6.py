# DESAFIO 01

# Faça um programa que mostre na tela uma contagem
# regressiva para o estouro de fogos de artificio, indo de 10 até 0,
# com uma pausa de 1 segundo entre eles.


# import time #time.sleep(5)  atraso de codigo
# for i in [10,9,8,7,6,5,4,3,2,1]:
#     print(i)
#     time.sleep(1)
#     if i==1:
#         break
# print("boom kabom bom kabooom")

# DESAFIO 02

# Crie um programa que mostre na tela todos os números pares
# que estão no intervalo entre 1 e 50.

# for i in range(0,51,2):
#     print(i)

    
# DESAFIO 03

# Faça um programa que calcule a soma entre todos os números
# ímpares que são múltiplos de três e que se encontram no
# intervalo de 1 até 500.

# soma=0
# for i in range(1,501,2):
#     if i%3==0: #e multiplo de 3
#         print(i)
#         soma=soma+i #vai fazer o calculo de todos os multiplos de 3
# print(f"soma = {soma}")

# DESAFIO 04

# Refaça o DESAFIO 09, mostrando a tabuada de um número
# que o usuário escolher, só que agora utilizando um laço for.

# DESAFIO 05

# Desenvolva um programa que leia seis números inteiros e
# mostre a soma apenas daqueles que forem pares. Se o valor
# digitado for impar desconsidere-o.



#atividade 1
# for i in range(0,101,2):
#     print(i)
# # 2
# # atividade 3
# somatoria=0
# qnt_analisadas=int(input("quantas pessoas pretende analisar? "))
# for i in range(1,qnt_analisadas+1):
#     temperatura=float(input("digite a temperatura: "))
#     somatoria=somatoria+temperatura
#     print(f"paciente {i}: ")
#     if temperatura<=37.2:
#         print("normal 👍")
#     elif temperatura>37.2 and temperatura<=38:
#         print("febriu 😢")
#     elif temperatura>38 and temperatura<=39:
#         print("febre 🤢")
#     else:
#         print("febre alta 🥵")
#     print("-------------------------")
# media=somatoria/i
# print(f"media de temperatura de {i} pessoas = {media}")