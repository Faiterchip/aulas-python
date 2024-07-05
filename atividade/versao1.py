def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc
def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"
def main():
    print("Calculadora de IMC (Índice de Massa Corporal)")
    print("-------------------------------------------")
    peso = float(input("Digite o seu peso em kg: "))
    altura = float(input("Digite a sua altura em metros: "))
    imc = calcular_imc(peso, altura)
    classificacao = classificar_imc(imc)
    print(f"Seu IMC é: {imc:.2f}")
    print(f"Classificação: {classificacao}")
if __name__ == "__main__":
    main()
