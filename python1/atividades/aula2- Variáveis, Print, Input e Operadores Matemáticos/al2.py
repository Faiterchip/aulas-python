print("senai")
ak="qwerty"

salario=1200
salarioBruto=2050.33 #camel case 
salario_bruto=3300.23 #snake case

print("salario = R$",salario)
salario=salario+150 #aumento do valor salario
print("salario atualizado = R$",salario) #printa o valor aumentado
texto=str(2)
texto2=int(3)
n1=20
n2=15
adiçao=n1+n2
print("soma =",str(n1+n2))
print("adicao =",adiçao)#adiçao
print(f"adicao = {n1+n2}")
print(f"adicao = {adiçao}")
sub=n1-n2
print("subtracao =",sub) #sub sem chaves com var
print(f"subtracao = {sub}") #sub com chaves e variavel
print(f"subtracao = {n1-n2}") #sub com chaves sem var
multi=n1*n2
print("multiplicacao =",multi) #multi
print(f"multiplicacao = {n1*n2}")
print(f"multiplicacao = {multi}")
divi=n1/n2
print("divisao =",divi) #divi
print(f"divisao = {n1/n2}")
print(f"divisao = {divi}")
divisaoInteira=n1//n2
operadorDePotencia=n1**n2
operadorModulo=n1%n2
print(f"multi 5*2 {5*2}")
print(f"potencia 5**2 {5**2}")
print(f"divi 5/2 {5/2}")
print(f"potencia 5%2 {5%2}")
print(operadorModulo)

print("***********")
numeroInteiro=int(input("digite um numero inteiro:")) #da pra digitar
print(f"numero digitado = {numeroInteiro}")
numerofloat=float(input("digite um numero decimal:"))
print(f"numero decimal digitado = {numerofloat}")
booleano=bool(input("digite um valor booleano:"))
print(f"booleano digitado = {booleano}")
string=str(input("digite um texto:"))

print(type(2.33)) #identificar o tipo
print(type(2))
print(type(True))
print(type("dim"))

variavelmisterio= 10/2<10  #fazer contas
print(type(variavelmisterio))
texxt="212"
print(texxt.isnumeric())
print(texxt.isalpha())
print(texxt.isalnum())
print(texxt.rjust)