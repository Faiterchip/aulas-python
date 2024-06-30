# #Crie um programa que leia dois numeros e mostra a soma entre eles.
numero1=int(input("digite um numero: "))
print(f"numero digitado = {numero1}")
numero2=int(input("digite outro numero: "))
print(f"outro numero digitado = {numero2}")
resultado=numero1+numero2
print("resultado = ",resultado)

# #Faça um programa que leia um número inteiro e mostra na tela
# #e seu sucessor e seu antecessor.
num1=int(input("digite um numero: "))
print(num1-1)
num2=int(input("digite outro numero: "))
print(num2+1)

# Crie um algoritmo que leia um número e mostre o seu dobro,
# triplo e o seu quadrado.
nume1=int(input("digite um numero: "))
print(f"o dobro deste numero é: {nume1*2} o triplo deste numero é: {nume1*3} e este numero ao quadrado é {nume1**nume1}")

# Desenvolva um programa que leia as duas notas de um aluno,
# calcule e mostra a sua média.
media1=int(input("digite sua nota: "))
media2=int(input("digite sou outra nota: "))
result=media1+media2
nota=result/2
print(f"sua nota é: {nota}")

# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostra quantos Dólares
# ela pode comprar.
# Considere o dólar = R$ 5,00
dinheiro=int(input("quanto voce tem: "))
print(f"voce tera {dinheiro/5} dolares")

# crie um programa para efetuar a leitura de um programa inteiro e aprensentar o quadrado deste numero
sim1=int(input("numero: "))
print(f"seu numero inteiro é {sim1} e o seu numero ao quadrado é {sim1**sim1}")

# escreva um programa que leia dois caracteres e imprima-os na tela da seguinte forma: o usuario digitou{caracter1} e {caracter2}!
caracter1=(input("digite alguma coisa: "))
caracter2=(input("digite outra coisa: "))
print(f"o usuario digitou: {caracter1} e {caracter2}!")

# crie um programa que leia um numero inteiro e imprimir seu sucessor e seu antecessor
caractere1=int(input("digite um numero"))
print(f"voce digitou {caractere1} o numero sucessor é: {caractere1+1} e o antecessor é {caractere1-1}")

# crie um programa para entrar com base a altura de um retangulo e imprimir respectivamente o perimetro e a area correspondente
# area=bxh
# perimetro=2b+2h
base=float(input("digite a base: "))
altura=float(input("digite a altura: "))
area=base*altura
perimetro=2*base+2*altura
print(f"Area do retangulo = {area}")
print(f"Perimetro do retangulo = {perimetro}")

# #prestaçao
valor=float(input("digite o valor da prestaçao: "))
tempo=float(input("digite o tempo de prestaçao (em dias): "))
taxa=float(input("digite a taxa de prestaçao: "))
prestacao=valor+(valor*(taxa/100)*tempo)
print(prestacao)
