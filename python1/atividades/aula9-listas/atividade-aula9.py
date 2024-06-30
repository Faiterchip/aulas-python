# DESAFIO 01-----------------------------------------------------------------------------------------------------------------------------
# Faça um programa que leia 5 valores numéricos e guarde-os
# em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as
# suas respectivas posições na lista.
# numeros=[]
# maior=menor=0
# for i in range(0,5):
#     numero=int(input(f"digite o {i+1} numero: "))
#     numeros.append(numero)
#     if i==0:
#         maior = menor = numero
#     else:
#         if numero>maior:
#             maior=numero
#         if numero<menor:
#             menor=numero
# print(f"numeros inseridos: {numeros} o maior é: {maior} e o menor é: {menor}")

# DESAFIO 02------------------------------------------------------------------------------------------------
# Crie um programa onde o usuário possa digitar vários valores
# numéricos e cadastre-os em uma lista. Caso o número já
# exista lá dentro, ele não será adicionado. No final serão
# exibidos todos os valores únicos digitados, em ordem
# crescente.

# valors=[]
# while True:
#     numero=int(input("digite um numero de 0 a 100 e digite -1 se quiser sair"))
#     print(" ")
#     if numero in valors:
#         print("numero ja cadastrado")
#     else:
#         valors.append(numero)
#         print(valors)
#     if numero==-1:
#         print("saindo")
#         break
# print(valors)

# DESAFIO 03-----------------------------------------------------------------------------------

# Crie um programa onde o usuário possa digitar cinco valores
# numéricos e cadastre-os em uma lista, já na sua posição
# correta de inserção (sem usar o sort()).

# No final mostre a lista ordenada na tela
# lista=[]
# for i in range(0,10):    #contador = 0-1-2
#     esk=int(input(f"digite o {i+1}° numero"))  #3-8-6
#     print(esk)
#     if i ==0 or esk >lista[-1]:#é maior?
#         lista.append(esk)
#     else:
#         pos=0
#         while pos < len(lista):#pos =0 e len = a 2  0<2?
#             if esk<=lista[pos]: #6<=3?
#                 lista.insert(pos,esk)
#                 print(f"adicionado {pos}")
#                 break
#             pos +=1
# print(f"os valores ordenados sao {lista}")
#lista[3,8]
# DESAFIO 04-------------------------------------------------------------------------------------

# Crie um programa que vai ler vários números e colocar em
# uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os
# valores pares e os valores impares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

# DESAFIO 07-----------------------------------------------------------------------------------
# Crie um programa que cria uma matriz de dimensão 3x3 e
# preencha com valores lidos pelo teclado.
# No final mostre a Matriz na tela, com a formatação correta.

# matriz=[[0,0,0],[0,0,0],[0,0,0]]
# c=0
# for i in matriz[0]:
#     numero=int(input(f"digite um valor para [0,{c}]:"))
#     matriz[0][c]=numero
#     c+=1
# for i in matriz[1]:
#     if c==3:
#         c=0
    
#     numero=int(input(f"digite um valor para [0,{c}]:"))
#     matriz[1][c]=numero
#     c+=1
# for i in matriz[2]:
#     if c==3:
#         c=0
    
#     numero=int(input(f"digite um valor para [0,{c}]:"))
#     matriz[2][c]=numero
#     c+=1
# print(matriz)
matriz=[[0,0,0],[0,0,0],[0,0,0]]
c=0
for i in range(0,3):
    for j in matriz[i]:
        if c==3:
            c=0
        numero=int(input(f"digite um valor para [{i},{c}]: "))
        matriz[1][c]=numero
        c+=1
print(matriz[0])
print(matriz[1])
print(matriz[2])