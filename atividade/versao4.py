import tkinter as tk
from tkinter import messagebox
def calcular_imc():
    peso = float(entry_peso.get())
    altura = float(entry_altura.get())
    imc = peso / (altura ** 2)
    classificacao = classificar_imc(imc)
    resultado_imc.set(f"IMC calculado: {imc:.2f} - Classificação: {classificacao}")
    if classificacao in pacientes:
        pacientes[classificacao] += 1
def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"
def analisar_dados():
    total_pacientes = sum(pacientes.values())
    if total_pacientes == 0:
        messagebox.showinfo("Análise de Dados", "Nenhum paciente foi analisado ainda.")
        return
    percentual_abaixo_peso = (pacientes["Abaixo do peso"] / total_pacientes) * 100
    percentual_peso_normal = (pacientes["Peso normal"] / total_pacientes) * 100
    percentual_sobrepeso = (pacientes["Sobrepeso"] / total_pacientes) * 100
    percentual_obesidade = (pacientes["Obesidade"] / total_pacientes) * 100
    mensagem = f"Total de pacientes analisados: {total_pacientes}\n\n"
    mensagem += f"Abaixo do peso: {pacientes['Abaixo do peso']} pacientes = {percentual_abaixo_peso:.2f}%\n"
    mensagem += f"Peso normal: {pacientes['Peso normal']} pacientes = {percentual_peso_normal:.2f}%\n"
    mensagem += f"Sobrepeso: {pacientes['Sobrepeso']} pacientes = {percentual_sobrepeso:.2f}%\n"
    mensagem += f"Obesidade: {pacientes['Obesidade']} pacientes = {percentual_obesidade:.2f}%"
    messagebox.showinfo("Análise de Dados", mensagem)
def fechar_programa():
    janela_principal.destroy()
janela_principal = tk.Tk()
janela_principal.title("Calculadora de IMC - Versão 4")
resultado_imc = tk.StringVar()
pacientes = {
    "Abaixo do peso": 0,
    "Peso normal": 0,
    "Sobrepeso": 0,
    "Obesidade": 0
}
label_instrucao = tk.Label(janela_principal, text="Digite o peso e a altura do paciente:")
label_instrucao.pack(pady=10)
frame_entrada = tk.Frame(janela_principal)
frame_entrada.pack()
label_peso = tk.Label(frame_entrada, text="Peso (kg):")
label_peso.grid(row=0, column=0, padx=5, pady=5)
entry_peso = tk.Entry(frame_entrada)
entry_peso.grid(row=0, column=1, padx=5, pady=5)
label_altura = tk.Label(frame_entrada, text="Altura (m):")
label_altura.grid(row=1, column=0, padx=5, pady=5)
entry_altura = tk.Entry(frame_entrada)
entry_altura.grid(row=1, column=1, padx=5, pady=5)
button_calcular_imc = tk.Button(janela_principal, text="Calcular IMC", command=calcular_imc)
button_calcular_imc.pack(pady=10)
label_resultado_imc = tk.Label(janela_principal, textvariable=resultado_imc)
label_resultado_imc.pack()
button_analisar_dados = tk.Button(janela_principal, text="Verificar análise dos dados", command=analisar_dados)
button_analisar_dados.pack(pady=10)
button_fechar = tk.Button(janela_principal, text="Sair", command=fechar_programa)
button_fechar.pack(pady=10)
janela_principal.mainloop()
