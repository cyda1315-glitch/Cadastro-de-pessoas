import tkinter as tk
from tkinter import messagebox, scrolledtext
import os
from datetime import datetime

def ir_para_telefone(event):
    entry_telefone.focus_set()

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
    entry_nome.focus_set()

def abrir_relatorio_diario():
    pasta_atual = os.path.dirname(os.path.abspath(__file__))
    data_hoje = datetime.now().strftime("%d/%m/%Y")
    
    texto_relatorio = f"--- RELATÓRIO DE CADASTROS DO DIA {data_hoje} ---\n\n"
    total_cadastros = 0
    
    for arquivo_nome in os.listdir(pasta_atual):
        if arquivo_nome.endswith(".txt"):
            caminho_completo = os.path.join(pasta_atual, arquivo_nome)
            
            with open(caminho_completo, "r", encoding="utf-8") as f:
                conteudo = f.read()
                
            blocos = conteudo.split("-" * 30)
            for bloco in blocos:
                
                if f"Data do Cadastro: {data_hoje}" in bloco:
                    texto_relatorio += bloco.strip() + "\n"
                    texto_relatorio += "-" * 30 + "\n\n"
                    total_cadastros += 1

    texto_relatorio += f"Total de novos cadastros hoje: {total_cadastros}"

    janela_relatorio = tk.Toplevel(janela)
    janela_relatorio.title(f"Relatório Diário - {data_hoje}")
    janela_relatorio.geometry("450x400")
    
    txt_area = scrolledtext.ScrolledText(janela_relatorio, width=50, height=22, font=("CourierNew", 10))
    txt_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    txt_area.insert(tk.INSERT, texto_relatorio)
    txt_area.configure(state='disabled') # Impede o usuário de apagar o texto do relatório

janela = tk.Tk()
janela.title("Cadastro de Clientes")
janela.geometry("350x280") # Aumentei um pouquinho a altura para acomodar o novo botão

lbl_nome = tk.Label(janela, text="Nome do Cliente:", font=("Arial", 10, "bold"))
lbl_nome.pack(pady=(15, 2))
entry_nome = tk.Entry(janela, width=35)
entry_nome.pack(pady=5)

entry_nome.bind("<Return>", ir_para_telefone)

lbl_telefone = tk.Label(janela, text="Telefone/Celular:", font=("Arial", 10, "bold"))
lbl_telefone.pack(pady=(10, 2))
entry_telefone = tk.Entry(janela, width=35)
entry_telefone.pack(pady=5)

entry_telefone.bind("<KeyRelease>", formatar_telefone)

frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=20)

btn_cadastrar = tk.Button(frame_botoes, text="Salvar Cadastro", command=salvar_cliente, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), padx=10)
btn_cadastrar.pack(side=tk.LEFT, padx=5)

btn_relatorio = tk.Button(frame_botoes, text="Relatório Diário", command=abrir_relatorio_diario, bg="#2196F3", fg="white", font=("Arial", 10, "bold"), padx=10)
btn_relatorio.pack(side=tk.LEFT, padx=5)

entry_nome.focus_set()

janela.mainloop()
