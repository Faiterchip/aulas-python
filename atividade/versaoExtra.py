import tkinter as tk
from tkinter import messagebox
def calcular_imc():
    nome = entry_nome.get()
    peso = float(entry_peso.get())
    altura = float(entry_altura.get())
    if peso <= 0 or altura <= 0:
        messagebox.showerror("Erro", "O peso e a altura devem ser valores positivos.")
        return
    imc = peso / (altura ** 2)
    resultado_imc = classificar_imc(imc)
    paciente = {
        "Nome": nome,
        "Peso": peso,
        "Altura": altura,
        "IMC": imc,
        "Resultado IMC": resultado_imc
    }
    pacientes.append(paciente)
    update_lista_pacientes()
    resultado_imc_text = f"IMC calculado: {imc:.2f} - Classificação: {resultado_imc}"
    resultado_imc.set(resultado_imc_text)
    entry_nome.delete(0, tk.END)
    entry_peso.delete(0, tk.END)
    entry_altura.delete(0, tk.END)
def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"
def visualizar_pacientes():
    if not pacientes:
        messagebox.showinfo("Visualizar Pacientes", "Não há pacientes registrados.")
        return
    mensagem = "Lista de Pacientes:\n\n"
    for paciente in pacientes:
        mensagem += f"Nome: {paciente['Nome']}, Peso: {paciente['Peso']}, Altura: {paciente['Altura']}, IMC: {paciente['IMC']:.2f}, Resultado IMC: {paciente['Resultado IMC']}\n"
    messagebox.showinfo("Visualizar Pacientes", mensagem)
def buscar_paciente():
    nome_busca = entry_busca.get().strip().lower()
    paciente_encontrado = False
    mensagem = ""
    for paciente in pacientes:
        if nome_busca == paciente['Nome'].lower():
            mensagem += f"Nome: {paciente['Nome']}, Peso: {paciente['Peso']}, Altura: {paciente['Altura']}, IMC: {paciente['IMC']:.2f}, Resultado IMC: {paciente['Resultado IMC']}\n"
            paciente_encontrado = True
    if not paciente_encontrado:
        mensagem = f"Paciente '{nome_busca}' não encontrado."
    messagebox.showinfo("Buscar Paciente", mensagem)
def update_lista_pacientes():
    # Limpar a exibição atual de pacientes na interface
    for widget in frame_lista_pacientes.winfo_children():
        widget.destroy()
    for i, paciente in enumerate(pacientes):
        label_paciente = tk.Label(frame_lista_pacientes, text=f"Paciente {i+1}: Nome: {paciente['Nome']}, Peso: {paciente['Peso']}, Altura: {paciente['Altura']}, IMC: {paciente['IMC']:.2f}, Resultado IMC: {paciente['Resultado IMC']}")
        label_paciente.pack(anchor=tk.W)
janela_principal = tk.Tk()
janela_principal.title("Calculadora de IMC - Versão Desafio Extra")
resultado_imc = tk.StringVar()
pacientes = []
label_instrucao = tk.Label(janela_principal, text="Digite o nome, peso e altura do paciente:")
label_instrucao.pack(pady=10)
frame_entrada = tk.Frame(janela_principal)
frame_entrada.pack()
label_nome = tk.Label(frame_entrada, text="Nome:")
label_nome.grid(row=0, column=0, padx=5, pady=5)
entry_nome = tk.Entry(frame_entrada)
entry_nome.grid(row=0, column=1, padx=5, pady=5)
label_peso = tk.Label(frame_entrada, text="Peso (kg):")
label_peso.grid(row=1, column=0, padx=5, pady=5)
entry_peso = tk.Entry(frame_entrada)
entry_peso.grid(row=1, column=1, padx=5, pady=5)
label_altura = tk.Label(frame_entrada, text="Altura (m):")
label_altura.grid(row=2, column=0, padx=5, pady=5)
entry_altura = tk.Entry(frame_entrada)
entry_altura.grid(row=2, column=1, padx=5, pady=5)
button_calcular_imc = tk.Button(janela_principal, text="Calcular IMC", command=calcular_imc)
button_calcular_imc.pack(pady=10)
label_resultado_imc = tk.Label(janela_principal, textvariable=resultado_imc)
label_resultado_imc.pack()
button_visualizar_pacientes = tk.Button(janela_principal, text="Visualizar Todos os Pacientes", command=visualizar_pacientes)
button_visualizar_pacientes.pack(pady=10)
label_busca = tk.Label(janela_principal, text="Buscar paciente pelo nome:")
label_busca.pack()
entry_busca = tk.Entry(janela_principal)
entry_busca.pack()
button_buscar_paciente = tk.Button(janela_principal, text="Buscar Paciente", command=buscar_paciente)
button_buscar_paciente.pack(pady=10)
frame_lista_pacientes = tk.Frame(janela_principal)
frame_lista_pacientes.pack(pady=10)
button_fechar = tk.Button(janela_principal, text="Sair", command=janela_principal.quit)
button_fechar.pack(pady=10)
janela_principal.mainloop()