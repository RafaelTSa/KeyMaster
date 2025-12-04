# 🔐 KeyMaster — Gerador de Senhas Seguras em Python

> 📚 Projeto desenvolvido durante o **Desafio de 21 Dias** da Comunidade Dev Completo.

---

## 📌 Sobre o Projeto

O **KeyMaster** é um gerador de senhas seguras desenvolvido em **Python**, com foco em:

- Boas práticas de segurança
- Organização e escalabilidade do código
- Usabilidade tanto em **linha de comando (CLI)** quanto em **interface gráfica (GUI)**

O projeto foi construído de forma **incremental**, evoluindo a cada dia do desafio, saindo de um script simples até uma aplicação desktop funcional.

---

## ⚙️ Funcionalidades

✅ Geração de senhas criptograficamente seguras com `secrets`  
✅ Definição do comprimento da senha (mínimo recomendado de 8 caracteres)  
✅ Escolha dos tipos de caracteres:
- Letras minúsculas  
- Letras maiúsculas  
- Números  
- Símbolos  

✅ Validação de entradas do usuário  
✅ Mensagens de erro amigáveis  
✅ Registro de eventos em arquivo de log  
✅ Opção de copiar a senha automaticamente para a área de transferência  
✅ Separação clara entre lógica, interface e execução  

---

## 🖥️ Interfaces Disponíveis

### 🔹 CLI — Linha de Comando

Permite gerar senhas diretamente pelo terminal, com perguntas interativas.

```bash
python -m keymaster.cli



🔹 GUI — Interface Gráfica (Tkinter)

Aplicação desktop simples e funcional com:

Campo para tamanho da senha

Checkboxes para seleção de caracteres

Botão para gerar senha

Exibição visual do resultado

python -m keymaster.gui




🛠️ Tecnologias Utilizadas

Python 3

Tkinter (interface gráfica)

secrets (geração segura de senhas)

logging (registro de eventos)

Git & GitHub (versionamento)


📂 Estrutura do Projeto
KeyMaster/
│
├── src/
│   └── keymaster/
│       ├── __init__.py
│       ├── cli.py        # Interface de linha de comando
│       ├── gui.py        # Interface gráfica (Tkinter)
│       └── generator.py # Lógica de geração de senhas
│
├── logs/
│   └── keymaster.log
│
├── .gitignore
└── README.md


▶️ Como Usar o KeyMaster

O KeyMaster pode ser utilizado de duas formas: linha de comando (CLI) ou interface gráfica (GUI).

🔧 Pré-requisitos

Python 3.10 ou superior instalado

Clonar o repositório:

git clone https://github.com/seu-usuario/keymaster.git
cd keymaster


💡 Não é necessário instalar bibliotecas externas — o projeto utiliza apenas bibliotecas padrão do Python.



🖥️ Opção 1 — Usando via Linha de Comando (CLI)

Execute o comando abaixo no terminal:
python -m keymaster.cli


Programa irá:
1. Solicitar o comprimento da senha
2. Perguntar se deseja usar:
    - Letras maiúsculas
    - Números
    - Símbolos
3. Gerar a senha com base nas opções escolhidas
4. Exibir a senha no terminal
5. Copiar automaticamente a senha para a área de transferência (se habilitado)
✅ Ideal para usuários que preferem rapidez no terminal.


🖱️ Opção 2 — Usando a Interface Gráfica (GUI)
Execute:
python -m keymaster.gui


Na interface gráfica, o usuário pode:
1. Informar o tamanho da senha
2. Marcar ou desmarcar os tipos de caracteres desejados
3. Clicar em “Gerar Senha”
4. Visualizar a senha gerada na tela
5. Ter a senha copiada automaticamente para a área de transferência
✅ Ideal para quem prefere uma experiência visual e simples.


📋 Copiar Senha Automaticamente
Após gerar uma senha:
- Ela é exibida na tela ou terminal
- E também copiada automaticamente para a área de transferência, facilitando o uso imediato


⚠️ Recomendações de Segurança

Utilize senhas com 8 ou mais caracteres
Combine letras, números e símbolos
Evite reutilizar senhas importantes



## 🖼️ Interface Gráfica

![Interface gráfica do KeyMaster](https://raw.githubusercontent.com/RafaelTSa/KeyMaster/main/src/keymaster/assets/screenshots/gui-screenshot.png)






🎯 Objetivo Educacional

Este projeto tem como objetivo praticar e consolidar:
Lógica de programação em Python
Boas práticas de organização de código
Separação de responsabilidades (CLI, GUI e lógica)
Uso de bibliotecas padrão do Python
Versionamento de código com Git

🚀 Próximas Melhorias (Ideias)
🔐 Indicador de força da senha
📦 Geração de executável (.exe)
🎨 Melhorias no layout da interface gráfica
🌐 Publicação de releases no GitHub


👨‍💻 Autor
Desenvolvido por Rafael Teixeira
📅 Desafio de 21 Dias — Comunidade Dev Completo