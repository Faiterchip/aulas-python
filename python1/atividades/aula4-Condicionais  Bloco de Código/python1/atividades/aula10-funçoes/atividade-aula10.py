# DESAFIO 01
# Faça um programa que leia o nome e média de um aluno,
# guardando também a situação em um dicionário. No final
# mostre o conteúdo da estrutura na tela.
# Reprovado se tiver nota < que 7

# meuDicionario ={}

# meuDicionario['nome']= str(input("Digite seu nome: "))
# meuDicionario['nota']= float(input("Digite sua Média: "))


# if meuDicionario['nota']>=7:
#     meuDicionario['situacao']= "Aprovado"
# elif meuDicionario['nota']>=5  and meuDicionario['nota']<7:
#     meuDicionario['situacao']= "Recuperação! - Tem salvação!"
# else:
#     meuDicionario['situacao']= "Reprovado - Se lascou!"
   
# print("=="*30)

# print(meuDicionario)

# print("=="*30)

# for k, v in meuDicionario.items():
#     print(f"O {k} é igual a {v}")
   

# print(f"O Nome é igual a {meuDicionario['nome']}")
# print(f"A Média é igual a {meuDicionario['nota']}")
# print(f"Sua Situação é {meuDicionario['situacao']}")

# DESAFIO 02
# Crie um programa onde 4 jogadores joguem um dado e
# tenham resultado aleatórios. Guarde esses resultados em um
# dicionário . No final, coloque esse dicionário em ordem,
# sabendo que o vencedor tirou o maior numero no dado

# from random import randint
# from time import sleep
# from operator import itemgetter

# meuDicionario = {
#     "jogador1" : randint(1,6),
#     "jogador2" : randint(1,6),
#     "jogador3" : randint(1,6),
#     "jogador4" : randint(1,6)
# }

# for k, v in meuDicionario.items():
#     print(f"{k} tirou {v} no dado")
#     sleep(1)

# # print(meuDicionario)

# print("Em ordem crescente")

# #sorted(iterable, key=key, reverse=reverse)
# #sorted(Quem?, qual a chave, Quer inveter?)
# ranking = sorted(meuDicionario.items(), key=itemgetter(1), reverse=True)
# print(ranking)

# for i, v in enumerate(ranking):
#     print(f"{i+1}° lugar: {v[0]} com {v[1]}")
#     sleep(1)

# # DESAFIO 03

# # Crie um programa que leia nome, ano de nascimento e
# # carteira de trabalho e cadastre-os (com idade) em um
# # dicionário se por acaso o CTPS for diferente de ZERO, o
# # dicionário receberá também o ano de contratação e o salário.
# # Calcule e acrescente, além da idade, com quantos anos a
# # pessoa vai se aposentar.
# # Sabendo que ele vai se aposentar após 35 anos de
# # colaboração.

# # Crie um programa que leia nome, ano de nascimento e
# # carteira de trabalho e cadastre-os (com idade) em um
# # dicionário se por acaso o CTPS for diferente de ZERO, o
# # dicionário receberá também o ano de contratação e o salário.
# # Calcule e acrescente, além da idade, com quantos anos a
# # pessoa vai se aposentar.

# # Sabendo que ele vai se aposentar após 35 anos de
# # colaboração.

# from datetime import date

# anoAtual = date.today().year
# tempoTrabalhado=0


# dicionario = {
#     'nome' : str(input("Nome: " )),
#     'Ano de Nascimento' : int(input("Ano de Nascimento: " )),
#     'Carteira de Trabalho' : int(input("Carteira de Trabalho (0 se não tem): " ))
# }

# print(dicionario)

# idade = anoAtual - dicionario['Ano de Nascimento']
# del dicionario['Ano de Nascimento']
# dicionario['Idade'] = idade

# print(dicionario)

# if dicionario['Carteira de Trabalho']== 0:
#     for k, v in dicionario.items():
#         # print(f"O {k} tem o valor {v}")
#         print(f" {k} = {v}")
# else:
#     dicionario['Ano Contratação'] = int(input("Ano de Contratação: " ))
#     dicionario['Salario'] = float(input("Digite seu salário: " ))
#     tempoTrabalhado = anoAtual - dicionario['Ano Contratação']
   
#     if tempoTrabalhado > 35:
#         dicionario['Aposentadoria'] = 'Aposentado'
#     else:
#         tempoAposentadoria = idade + (35 - tempoTrabalhado)
#         dicionario['Aposentadoria'] = tempoAposentadoria
       
#     for k, v in dicionario.items():
#         print(f"- {k} tem o valor {v}")
        
# DESAFIO 04
# Crie um programa que gerencie o aproveitamento de um
# jogador de futebol. O programa vai ler o nome do jogador e
# quantas partidas ele jogou. Depois vai ler a quantidade de
# gols feitos em cada partida. No final, tudo isso será guardado
# em um dicionário, incluindo o total de gols feitos durante o
# campeonato.
dic={}
dic["nome"]=input("digite sseu nome: ")
dic["partidas"]=int(input("numero de partidas: "))
listagolls=[]
for i in range(0,dic["partidas"]):
    drr=int(input(f"numero de golls na {i+1} jogo: "))
    listagolls.append(drr)
dic["golls"]=listagolls
dic["total"]=sum(listagolls)#somatoria da lista---
print(dic)

# DESAFIO 05

# Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de casa pessoa em um dicionário e todos os
# dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) A média de idade do grupo.
# C) Uma lista com todas as mulheres.
# D) Uma lista com todas as pessoas com idade acima da média.