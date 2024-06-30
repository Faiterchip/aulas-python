# nome="felipe gomes"
# idade=16
# cidade="mogi das cruzes -sp"
# formacao="aprendendo python"
# print(f"ola eu me chamo {nome} tenho {idade} anos moro em {cidade} e estou {formacao}")
# import random
# numeross=123456
# valors=[]
# while True:
#     numeros=random.randint(0,100000000)
#     print(numeros)
#     valors.append(numeros)
    
    
#     print(" ")
#     if numeros in valors:
#         print("numero ja cadastrado")
#     else:
#         valors.append(numeros)
#         print(valors)
#     if numeros==numeross:
#         print("saindo")
#         break
# print(valors)
# while True:
#     print("h")
#     while True:
#         print("h")
#         while True:
#             print("h")
#             while True:
#                 print("h")
#                 while True:
#                     print("h")
#                     while True:
#                         print("h")
#                         while True:
#                             print("h")
#                             while True:
#                                 print("h")
#                                 while True:
#                                     print("h")
#                                     while True:
#                                         print("h")
#                                         while True:
#                                             print("h")
#                                             while True:
#                                                 print("h")
#                                                 while True:
#                                                     print("h")
#                                                     while True:
#                                                         print("h")
#                                                         while True:
#                                                             print("h")
#                                                             while True:
#                                                                 print("h")
produtos={"cadeira":100,
                "headset":250,
                "pc":1300
}
while True:
    pe=input("nome do produto: ")
    if pe=="fim":
        break
    if pe in produtos:
        print(f"o {produtos} custa {produtos.values} reais ")
    else:
        print("produto nao encontrado")