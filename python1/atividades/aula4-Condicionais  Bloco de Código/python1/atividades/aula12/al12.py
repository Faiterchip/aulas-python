try:
    #o bloco de codigo pode gerar exceções
    numero=int(input("digite um numero"))
    resultado=10/numero
except(ValueError,TypeError):
    #trata exceções de valueError e TypeError
    print("voce deve digitar um numero valido. ")
except ZeroDivisionError:
    #trata exceção de zerodivisionError
    print("nao é possivel dividir por zero. ")
else:
    #executado sem nenhum erro ocorrer
    print("resultado:",resultado)
finally:
    #sempre executado, independentemente de exceções
    print("encerrando o programa. ")