# def mundo():             #guarda o arqivo ate ser chamado
#     print("ola mundo")
#     return     #retorna so o resultado

# nome=input("digite seu nome")
# mundo()        #arquivo sendo chamado
# variavel=5
# def funcao():
#     global variavel
#     variavel=10
#     print(variavel)
# def tese():
#     global variavel
#     soma=variavel+2
#     return soma
# funcao()
# print(variavel)
# print("=="*30)
def tabuada(numero):
    print(f"tabuada do {numero}: ")
    for i in range(1,11):
        resultado=numero*i
        print(f"{numero} X {i} = {resultado}")
tabuada(7)
digt=int(input("digite um numero: "))
digto=int(input("digite o fim: "))
def tabuada(digt):
    print(f"tabuada do {digt}: ")
    for i in range(1,digto+1):
        resultado=digt*i
        print(f"{digt} X {i} = {resultado}")
tabuada(digt)

def tabuada(numero):
    print(f"tabuada do {numero}: ")
    for i in range(1,11):
        resultado=numero*i
        print(f"{numero} X {i} = {resultado}")
tabuada(7)

# def tabuada(numero):
#     print(f"tabuada do {numero}: ")
#     for i in range(1,11):
#         resultado=numero*i
#         print(f"{numero} X {i} = {resultado}")
# tabuada(7)

def contador(*num):
    print(num)
contador()