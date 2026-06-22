import tkinter as tk
from tkinter import messagebox
import os
from datetime import datetime

# Função para passar o foco do Nome para o Telefone ao apertar ENTER
def ir_para_telefone(event):
    entry_telefone.focus_set()

# Função para formatar o telefone automaticamente enquanto digita
def formatar_telefone(event):
    texto = entry_telefone.get()
    apenas_numeros = "".join([char for char in texto if char.isdigit()])
    apenas_numeros = apenas_numeros[:11]
    
    formato = ""
    if len(apenas_numeros) > 0:
        formato += f"({apenas_numeros[:2]}"
    if len(apenas_numeros) > 2:
        formato += f") {apenas_numeros[2:7]}"
    if len(apenas_numeros) > 7:
        formato += f"-{apenas_numeros[7:11]}"
        
    entry_telefone.delete(0, tk.END)
    entry_telefone.insert(0, formato)

# Função para salvar os dados no arquivo TXT personalizado
def salvar_cliente():
    nome = entry_nome.get().strip()
    telefone = entry_telefone.get().strip()
    
    if nome == "" or telefone == "":
        messagebox.showwarning("Aviso", "Por favor, preencha todos os campos!")
        return

    pasta_atual = os.path.dirname(os.path.abspath(__file__))
    nome_arquivo_limpo = nome.lower().replace(" ", "_")
    caminho_arquivo = os.path.join(pasta_atual, f"{nome_arquivo_limpo}.txt")
    
    data_hora_atual = datetime.now().strftime("%d/%m/%Y às %H:%M:%S")

    with open(caminho_arquivo, "a", encoding="utf-8") as arquivo:
        arquivo.write(f"Data do Cadastro: {data_hora_atual}\n")
        arquivo.write(f"Nome: {nome}\n")
        arquivo.write(f"Telefone: {telefone}\n")
        arquivo.write("-" * 30 + "\n")
    
    messagebox.showinfo("Sucesso", f"Cadastro de '{nome}' salvo com sucesso!\n\nArquivo gerado:\n{nome_arquivo_limpo}.txt")
    
    entry_nome.delete(0, tk.END)
    entry_telefone.delete(0, tk.END)
    # Devolve o cursor para o campo de nome para o próximo cadastro
    entry_nome.focus_set()

# --- Configuração da Interface Gráfica ---
janela = tk.Tk()
janela.title("Cadastro de Clientes")
janela.geometry("350x240")

# Rótulo e Campo para o Nome
lbl_nome = tk.Label(janela, text="Nome do Cliente:", font=("Arial", 10, "bold"))
lbl_nome.pack(pady=(15, 2))
entry_nome = tk.Entry(janela, width=35)
entry_nome.pack(pady=5)

# --- MUDANÇA AQUI: Ativa o ENTER no campo de nome ---
entry_nome.bind("<Return>", ir_para_telefone)

# Rótulo e Campo para o Telefone
lbl_telefone = tk.Label(janela, text="Telefone/Celular:", font=("Arial", 10, "bold"))
lbl_telefone.pack(pady=(10, 2))
entry_telefone = tk.Entry(janela, width=35)
entry_telefone.pack(pady=5)

entry_telefone.bind("<KeyRelease>", formatar_telefone)

# Botão de Cadastrar
btn_cadastrar = tk.Button(janela, text="Salvar Cadastro", command=salvar_cliente, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
btn_cadastrar.pack(pady=20)

# Define o foco inicial direto no campo de nome ao abrir o programa
entry_nome.focus_set()

janela.mainloop()