# Sistema de Cadastro de Clientes em Python 📝

Este é um projeto simples e intuitivo para cadastro de clientes utilizando uma interface gráfica integrada com salvamento de dados em arquivos de texto (`.txt`) individuais e personalizados.

## 🚀 Funcionalidades

* **Interface Gráfica:** Desenvolvida em Tkinter para facilitar o uso.
* **Formatação Automática:** O campo de telefone aplica a máscara `(65) 99999-9999` automaticamente enquanto você digita.
* **Navegação Rápida:** Ao preencher o nome e apertar `ENTER`, o cursor pula direto para o campo do telefone.
* **Organização por Arquivos:** Cada cliente gera um arquivo `.txt` próprio com o seu nome (ex: `cida_silva.txt`).
* **Registro de Data e Hora:** O sistema grava o momento exato em que o cadastro foi realizado.

---

## 🛠️ Como rodar o projeto na sua máquina

Siga os passos abaixo para executar o sistema no seu computador através do VS Code:

### 1. Pré-requisitos
Certifique-se de ter o Python instalado na sua máquina. 
* *Nota: Este projeto utiliza o ecossistema padrão do Python (Tkinter), não sendo necessária a instalação de nenhuma biblioteca externa.*

### 2. Passo a Passo para Execução

1. **Abra a pasta do projeto** no seu VS Code (Vá em `File > Open Folder` e selecione a pasta do projeto).
2. Abra o arquivo principal chamado **`Cadastro.py`**.
3. Se o terminal do VS Code estiver aberto em uma pasta antiga do sistema, clique no ícone da **Lixeira** no canto direito do terminal para fechá-lo.
4. Clique no botão de **Play** (no canto superior direito do VS Code) para iniciar o programa com o caminho correto.

---

## 💻 Como usar o sistema

1. Digite o **Nome do Cliente** no primeiro campo.
2. Aperte a tecla **ENTER** no seu teclado (o cursor irá pular automaticamente para o campo de telefone).
3. Digite apenas os números do **Telefone/Celular** (os parênteses e o hífen aparecerão sozinhos).
4. Clique no botão **Salvar Cadastro**.
5. Uma mensagem de confirmação aparecerá e os dados serão salvos em um arquivo `.txt` localizado na mesma pasta do script!
