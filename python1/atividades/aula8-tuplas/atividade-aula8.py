# DESAFIO 01

# Crie um programa que tenha uma tupla totalmente preenchida com
# uma contagem por extenso, de zero até vinte.

# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e
# mostra-lo por extenso.

# numeros=('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','catorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
# player=int(input("digite um numero entre 0,20 "))
# print(f"{numeros[player]}")

# DESAFIO 02

# Crie um programa que vai gerar cinco números aleatórios e colocar
# em uma tupla.
import random
# Depois disso, mostre a listagem de números gerados e também
# indique o menor e o maior valor que estão na Tupla.

# maior=0
# menor=0
# minhaLIsta=[]
# for i in range (1,6):
#     numeroAleatorio=random.randint(1,5)
#     minhaLIsta.append(numeroAleatorio)
# print(minhaLIsta)
# maior=max(minhaLIsta)
# menor=min(minhaLIsta)
# minhatuopla=tuple(minhaLIsta)
# print(f"maior = {maior}")
# print(f"menor = {menor}")
# print(f"lista = {minhatuopla}")

#  DESAFIO 03

# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela
# do Campeonato Brasileiro Serie B de Futebol, na ordem de
# colocação. Depois mostre:
# A) Apenas os 5 primeiros colocados.
# B) Os últimos 4 colocados da tabela.
# C) Uma lista com os times em ordem alfabética.
# D) Em que posição na tabela está o time do Santos.

# serieB = ('AMÉRICA-MG','GOIÁS','MIRASSOL','AVAÍ','SANTOS','SPORT','CEARÁ','OPERÁRIO','CORITIBA',
#           'VILA NOVA','NOVOROZONTINO','AMAZONAS','CHAPECOENSE','PONTE PRETA','CRB','PAYSANDU','BOTAFOGO','ITUANO','BRUSQUE','GUARANI')
# top5=serieB[:5]
# ultimos=serieB[-4:]
# print(f"5 primeiros colocados = {top5}")
# print(f"4 ultimos colocados = {ultimos}")
# ordem=sorted(serieB)
# posicao=serieB.index('SANTOS')
# print(f"ordem alfabetica = {ordem}")
# print(f"posiçao do santos = {posicao}")

# # DESAFIO 04

# Desenvolva um programa que leia quatro valores pelo teclado e
# guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram o números pares.

# numeros = (int(input('Digite um número: ')),int(input('Digite um número: ')),int(input('Digite um número: ')),\
#             int(input('Digite um número: ')),int(input('Digite um número: ')))

# #Quantas vezes o "9" aparece
# print(f"O valor 9 apareceu {numeros.count(9)} vezes")

# ##Mostra a posição do "3" se ele existir
# if 3 in numeros:
#     print(f"O valor 3 esta na {numeros.index(3)+1}° posicao")
# else:
#     print(f"O valor 3 não aparece nessa tupla")

# print(f"Os valores pares são ", end='') #end = faz espacos 

# ##Imprime apenas os Pares da Tupla
# for n in numeros:
#     if n % 2 == 0:    
#         print(n, end=' ')
#atividade 5
produtos= ("sofa",800.00,"geladeira",700.00,"fogão",700.00,"forno",300.00)
tamanho=len(produtos)
print(f"produto -------------- preço")
# print(f"{produtos[0]} --------------- {produtos[1]}") #manual
for i in range(0,tamanho,2):
    print(f"{produtos[i]} --------------- R${produtos[i+1]}") #automatico