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
    print("Calculadora de IMC (Índice de Massa Corporal) - Versão 2")
    print("------------------------------------------------------")
    pacientes_analisados = 0
    abaixo_peso = 0
    peso_normal = 0
    sobrepeso = 0
    obesidade = 0
    while True:
        peso = float(input("Digite o peso do paciente em kg (ou digite 0 para encerrar): "))
        if peso == 0:
            break
        altura = float(input("Digite a altura do paciente em metros: "))
        imc = calcular_imc(peso, altura)
        classificacao = classificar_imc(imc)
        pacientes_analisados += 1
        if classificacao == "Abaixo do peso":
            abaixo_peso += 1
        elif classificacao == "Peso normal":
            peso_normal += 1
        elif classificacao == "Sobrepeso":
            sobrepeso += 1
        elif classificacao == "Obesidade":
            obesidade += 1
    total_pacientes = pacientes_analisados
    percentual_abaixo_peso = (abaixo_peso / total_pacientes) * 100 if total_pacientes > 0 else 0
    percentual_peso_normal = (peso_normal / total_pacientes) * 100 if total_pacientes > 0 else 0
    percentual_sobrepeso = (sobrepeso / total_pacientes) * 100 if total_pacientes > 0 else 0
    percentual_obesidade = (obesidade / total_pacientes) * 100 if total_pacientes > 0 else 0
    print("\nAnálise final:")
    print(f"Total de pacientes analisados: {total_pacientes}")
    print(f"Abaixo do peso: {abaixo_peso} pacientes = {percentual_abaixo_peso:.2f}%")
    print(f"Peso normal: {peso_normal} pacientes = {percentual_peso_normal:.2f}%")
    print(f"Sobrepeso: {sobrepeso} pacientes = {percentual_sobrepeso:.2f}%")
    print(f"Obesidade: {obesidade} pacientes = {percentual_obesidade:.2f}%")
if __name__ == "__main__":
    main()
