# Crie um programa que leia o nome completo de uma pessoas
# e mostre

# O nome com todas as letras maiúsculas
# O nome com todas as letras minúsculas
# Quantas letras ao todo (sem considerar espaços)
# Quantas letras tem o primeiro nome

# nomeCompleto= input("Digite o seu nome completo: ")
# print(f"Nome Maiusculo: {nomeCompleto.upper()}")
# print(f"Nome Minusculo: {nomeCompleto.lower()}")

# print(f"Seu Nome Completo possui: {len(nomeCompleto)} caracteres")
# nomeCompletoSemEspaco = nomeCompleto.replace(" ","")
# print(f"Seu Nome Completo possui: {len(nomeCompletoSemEspaco)} letras")


# arrayNome = nomeCompleto.split()
# primeiroNome = arrayNome[0]
# print(f"Seu Primeiro Nome possui: {len(primeiroNome)}")


# Crie um programa que leia o nome de uma cidade e siga se ela
# começa ou não com o nome “Santo”.

text=input("digite sua cidade: ")
test=text.split()
tese=test[0].upper()
very="SANTOS"in tese
print(f"a cidade {text} tem santos no nome: {very}")

# Crie um programa que leia o nome de uma pessoa e diga se ela
# tem "Silva" no nome

pessoa=input("digite seu nome")
print(f"{pessoa.find('Silva')}")