texto="curso de python"  
print(" ")
print("fatiamento de string")#fatiamento de string
print(" ")
print(texto[4]) #imprime a letra da posicao 4
print(texto[6:8]) # imprima "de"
print(texto[9:15:2]) #imprima pto
print(texto[9:15]) #imprima python
print(texto[:5]) #curso
print(texto[9:]) #python
print(" ")
print("analise de string")
print(" ")
print(len(texto)) #conta tamanho string (15)
print(texto.count("o")) #conta qts vezes a letra o aparece
print(f"existe python?: {texto.find('python')}") #9 encontrar a palavra
print(f"existe python?: {texto.find('python ')}") #-1 pq nao encontrou
print(f"existe python?: {texto.find(' python')}") #8 espaço conta como letra

print(f"{'python' in texto}") # indica se tem a palavra no texto

print(f"{'python ' in texto}") #espaço conta como letra
print(" ")
print("transformaçao de string")
print(" ")
trocatexto=texto.replace("python","javascript") #troca um texto existente pelo outro
print(trocatexto)
print(f"temos {texto} e {trocatexto}, venha estudar \n com a gente!!!") #\n pula linha

textousuario=(input("gaga"))
textoMinusculo=texto.lower() #letra minuscula 
print(textoMinusculo)
textoMaiusculo=texto.upper() #letra maiuscula
print(textoMaiusculo)

textoCapitalizado=texto.capitalize() #primeira letra maiuscula
textoTitulo=texto.title() #titulo
print(textoCapitalizado)
print(textoTitulo)
texto2="  senai 1"
texto_sem_espaco=texto2.strip() #texto sem espaco espaços inuteis
print(texto2) #espaço
print(texto_sem_espaco) #sem

juntaTexto='-'.join(texto)
print(juntaTexto)

divideTexto=texto.split() #divide espaços dos textos
print(divideTexto)