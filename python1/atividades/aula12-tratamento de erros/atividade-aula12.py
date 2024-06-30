# DESAFIO 01
# Escreva um programa que peça ao usuário para digitar dois
# números e divida o primeiro número pelo segundo. Certifique-se
# de lidar com a possibilidade de divisão por zero.
# try:
#     valor=float(input("digite um numero"))
#     valor2=float(input("digite outro numero"))
#     print(f"o resultado foi: {valor/valor2}")
# except ZeroDivisionError:
#     print("nao da para dividir por zero")
 
# DESAFIO 02
# Escreva um programa que leia um arquivo de texto chamado
# "dados.txt" e exiba seu conteúdo. Certifique-se de lidar com o
# erro caso o arquivo não exista.

def ler_arquivo(nome_arquivo):
    try:
        with open('dados.txt', 'r') as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
    except FileNotFoundError:
        print(f"Erro: o arquivo '{nome_arquivo}' não foi encontrado.")
    except Exception as e: #exception = nao sabe qual erro vai dar
        print(f"Ocorreu um erro inesperado: {e}")
    else:
        print("ssss")

# Chamada da função para ler o arquivo "dados.txt"
ler_arquivo("dados.txt")

# DESAFIO 03
# Escreva um programa que solicite ao usuário para digitar um
# número inteiro e exiba o resultado da sua raiz quadrada. Lide
# com o erro caso o número seja negativo.

import math
try:
    num=int(input("digite um numero inteiro"))
    if num<0:
        raise ValueError("numero errado")
    raiz_quadrada=math.sqrt(num)
    print(f"a raiz quadrada de {num} e {raiz_quadrada}")
except Exception as error:
    print("ii")

# DESAFIO 04
# Escreva um programa que peça ao usuário para digitar seu
# nome e idade. Em seguida, exiba uma mensagem
# personalizada que inclua o nome e a idade. Lide com o erro
# caso a idade digitada não seja um número.