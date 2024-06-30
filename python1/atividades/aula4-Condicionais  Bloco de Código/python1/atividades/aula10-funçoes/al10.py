#lista de personagems
meu_dicionario={"nome":"bob",
                "sobrenome":"esponja",
                "idade":13
}
print(meu_dicionario) #{'nome': 'bob', 'sobrenome': 'esponja', 'idade': 13}
print(meu_dicionario.items()) #dict_items([('nome', 'bob'), ('sobrenome', 'esponja'), ('idade', 13)])
print(meu_dicionario.values()) #dict_values(['bob', 'esponja', 13])
print(meu_dicionario.keys()) #dict_keys(['nome', 'sobrenome', 'idade'])

meu_dicionario2=[{"nome":"bob",
                "sobrenome":"esponja",
                "idade":13
                },
{"nome":"jhony",
                "sobrenome":"bravo",
                "idade":35
                },
{"nome":"a",
                "sobrenome":"tc",
                "idade":90
}
]
print(meu_dicionario2[0].values())
print(meu_dicionario2[0]["nome"])
print(meu_dicionario2[1]["sobrenome"])
print(meu_dicionario2[2]["idade"])
for k,j in meu_dicionario.items():
    print(f"o {k} favorito é {j}")#o nome favorito é bob o sobrenome favorito é esponja o idade favorito é 13
    
estado={}
brasil=list()
for i in range(0,2):
    estado["uf"]=str(input("unidade federativa: "))
    estado["sigla"]=str(input("sigla do estado: "))
    brasil.append(estado.copy())
print(estado)
print(brasil)