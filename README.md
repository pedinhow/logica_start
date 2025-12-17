# 🚀 LógicaStart – Recurso Educacional Aberto de Lógica de Programação

O **LógicaStart** é um **Recurso Educacional Aberto (REA)** criado para ensinar **Lógica de Programação** a alunos do **Ensino Médio**, de forma acessível, prática e contextualizada.

O projeto utiliza **Python 3** com **Flask** e **Banco de Dados** para oferecer uma experiência completa com login, acompanhamento de progresso e certificação, sem perder a simplicidade de uso.

---

## 📖 Sobre o Projeto

O LógicaStart é uma aplicação web educacional que apresenta conceitos de programação em **pílulas de aprendizado (microlearning)**. Diferente de sites estáticos, ele agora permite que o aluno:

1.  **Crie uma conta simplificada** (apenas com o nome).
2.  **Acompanhe seu progresso** através de um Dashboard interativo.
3.  **Receba um certificado** ao concluir todos os módulos.

Todo o conteúdo didático continua centralizado em um único arquivo (`app/content.py`), facilitando a adaptação do material por professores.

---

## 🎯 Público-Alvo

* Estudantes do **Ensino Médio**
* Professores de **Informática, Pensamento Computacional ou Lógica**
* Projetos educacionais e iniciativas de extensão

---

## 🛠️ Tecnologias Utilizadas

### Informações do Sistema

* **Backend:** Flask (Python 3) + SQLAlchemy
* **Frontend:** HTML5 + Jinja2
* **Estilização:** Bootstrap 5 (Mobile-First)
* **Banco de Dados:** SQLite (Automático e Local)
* **Estrutura de Conteúdo:** Dicionário Python centralizado no arquivo `app/content.py`

> 📌 O banco de dados é criado automaticamente na primeira execução. Não é necessário instalar softwares adicionais de banco de dados (como MySQL ou Postgres) para rodar localmente.

---

## 📚 Conteúdo Abordado

O projeto cobre os principais pilares da lógica de programação:

1. Variáveis e Tipos de Dados
2. Entrada e Saída de Dados
3. Estruturas Condicionais (`if / else`)
4. Laços de Repetição (`while` e `for`)
5. Estruturas de Dados Básicas (listas)
6. Funções e Modularização
7. Depuração de Código

---

## 🚀 Guia de Instalação

### Passo 1 – Baixar o Projeto

1. Clique no botão **Code** (ou **Código**) neste repositório.
2. Escolha a opção **Download ZIP**.
3. Extraia o arquivo ZIP em uma pasta do seu computador.

---

### Passo 2 – Instalar o Python

1. Acesse o site oficial do Python:
   👉 [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Baixe a versão mais recente do **Python 3**.
3. Durante a instalação, marque a opção:
   **☑ Add Python to PATH**

---

### Passo 3 – Abrir o Terminal

* **Windows:** Abra o *Prompt de Comando* ou *PowerShell*
* **Linux / macOS:** Abra o *Terminal*

Navegue até a pasta onde você extraiu o projeto.

---

### Passo 4 – Instalar as Dependências

No terminal, digite o comando abaixo e pressione **Enter**:

```bash
pip install -r requirements.txt
```

---

### Passo 5 – Rodar o Projeto

Ainda no terminal, execute:

```bash
python app.py
```

Se tudo deu certo, aparecerá uma mensagem indicando que o servidor está rodando.

Abra o navegador e acesse:
👉 [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🧭 Onde Praticar?

Você pode aprender e praticar Python em diferentes ambientes. Escolha o que fizer mais sentido para você:

### 🖥️ Thonny

* Ideal para quem quer instalar um programa simples no computador.
* Interface limpa e pensada para iniciantes.
* Site: [https://thonny.org/](https://thonny.org/)

---

### 📒 Jupyter Notebook / Google Colab

* Aprendizado por **blocos de código + explicações**.
* Excelente para aulas e anotações.
* Google Colab roda direto no navegador, sem instalar nada.
* Colab: [https://colab.research.google.com/](https://colab.research.google.com/)

---

### 📱 Replit

* Funciona direto no navegador.
* Ótima opção para celular ou tablet.
* Ideal para quem não pode instalar programas.
* Site: [https://replit.com/](https://replit.com/)

---

## 🤝 Projeto como REA – Como Contribuir

O LógicaStart é um **Recurso Educacional Aberto**, ou seja, qualquer professor/educador pode:

* Adaptar os exemplos para sua realidade
* Alterar a linguagem pedagógica
* Criar novos módulos

### ✏️ Editando o Conteúdo

Todo o conteúdo do site está em um único arquivo:

```
content.py
```

Esse arquivo contém um **dicionário Python** com os módulos, textos e exemplos.

👉 Para mudar o conteúdo do site:

* Basta editar os textos dentro do dicionário
* Não é necessário mexer no código do servidor (`app.py`)
* Não é preciso saber Flask ou HTML

Isso torna o projeto ideal para professores que desejam **customizar o material didático**.

---

## 👥 Autores

* Carlos Magno II Regis Ramos
* Pedro Henrique Teixeira Torres
