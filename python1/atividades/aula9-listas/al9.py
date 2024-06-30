minhaLista=[1,2,2,3,4,5,6,7]
print(minhaLista) #mostra tudo
print(minhaLista[3]) #4
print(minhaLista[-1]) #mostra o ultimo
minhaLista[-1]="senai" #substitui o ultimo
minhaLista.append(1010) #adiciona no ultimo
print(minhaLista)
minhaLista.insert(1,2) #colocar posiçao e valor
print(minhaLista)  #insert(posiçao, valor)
minhaLista.remove(3) #remove o valor
# print(f"ordena crescente: {minhaLista.sort()}")
# print(f"ordena decrescente: {minhaLista.reverse()}")
# minhaLista.sort()
# minhaLista.reverse
print(minhaLista.count(2)) #conta quantos tem
excluido=minhaLista.pop() #removeu 1
print(f"removido= {excluido}") #exibe 1

del minhaLista[4:6] #remove posiçao 4 e 5
print(minhaLista)
minhaLista.clear() #limpa tudo
print(minhaLista)

comprar= [2.99,5.75,12.50,["macarrao","toddy","bom bom"]]
print(comprar) #[2.99, 5.75, 12.5, ['macarrao', 'toddy', 'bom bom']]
totalComprar=comprar[0]+comprar[1]+comprar[2]
print(f"total de compra = R$ {totalComprar}")
letras=['a','b','c']
num=[1,2,3]
total=[letras,num]
print(total)
total2=[letras+num]
print(total2)

minhaLista.index(2) #acha o primeiro numero 2 que aparecer