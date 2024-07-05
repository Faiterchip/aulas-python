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
def analisar_dados(pacientes):
    total_pacientes = sum(pacientes.values())
    if total_pacientes == 0:
        print("Nenhum paciente foi analisado ainda.")
        return
    percentual_abaixo_peso = (pacientes["Abaixo do peso"] / total_pacientes) * 100
    percentual_peso_normal = (pacientes["Peso normal"] / total_pacientes) * 100
    percentual_sobrepeso = (pacientes["Sobrepeso"] / total_pacientes) * 100
    percentual_obesidade = (pacientes["Obesidade"] / total_pacientes) * 100
    print("\nAnálise dos dados:")
    print(f"Total de pacientes analisados: {total_pacientes}")
    print(f"Abaixo do peso: {pacientes['Abaixo do peso']} pacientes = {percentual_abaixo_peso:.2f}%")
    print(f"Peso normal: {pacientes['Peso normal']} pacientes = {percentual_peso_normal:.2f}%")
    print(f"Sobrepeso: {pacientes['Sobrepeso']} pacientes = {percentual_sobrepeso:.2f}%")
    print(f"Obesidade: {pacientes['Obesidade']} pacientes = {percentual_obesidade:.2f}%")
def main():
    print("Calculadora de IMC (Índice de Massa Corporal) - Versão 3")
    print("--------------------------------------------------------")
    pacientes = {
        "Abaixo do peso": 0,
        "Peso normal": 0,
        "Sobrepeso": 0,
        "Obesidade": 0
    }
    while True:
        print("\nMenu:")
        print("1 - Calculadora de IMC")
        print("2 - Verificar análise dos dados")
        print("3 - Sair")
        escolha = input("Escolha uma opção (1/2/3): ")
        if escolha == "1":
            peso = float(input("Digite o peso do paciente em kg: "))
            altura = float(input("Digite a altura do paciente em metros: "))
            imc = calcular_imc(peso, altura)
            classificacao = classificar_imc(imc)
            print(f"IMC calculado: {imc:.2f} - Classificação: {classificacao}")
            if classificacao in pacientes:
                pacientes[classificacao] += 1
        elif escolha == "2":
            analisar_dados(pacientes)
        elif escolha == "3":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
if __name__ == "__main__":
    main()
