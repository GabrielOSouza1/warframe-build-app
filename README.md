# ⚔️ Warframe Build App

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-2.x-lightgrey?logo=flask)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow)
![License](https://img.shields.io/badge/Licença-Educacional-green)

> Projeto web em desenvolvimento para aprendizado, utilizando a metodologia **Scrum**.  
> O objetivo é permitir que jogadores de **Warframe** possam **criar, gerenciar e compartilhar suas builds**.

---

## 🚀 Tecnologias Utilizadas

- 🐍 **Python** – Linguagem de programação principal  
- 🌐 **Flask** – Micro-framework web para criar servidor e rotas  
- 🖼️ **Jinja** – Motor de templates para exibir dados dinâmicos  
- 🔗 **Requests** – Biblioteca para requisições HTTP e conexão com a API do Warframe  
- 💻 **Git & GitHub** – Controle de versão e hospedagem do código  

---

## 📌 Status do Projeto

✅ **Configuração do Ambiente** – Python + Flask configurados  
✅ **Servidor Web** – Servidor Flask em execução  
✅ **Requisição à API** – Conexão com API do Warframe exibindo lista de Warframes  
✅ **Estrutura de Rotas** – Página inicial e rota para builds criadas  
✅ **Estilização Básica** – Layout inicial com CSS  

---

## 🛠️ Próximos Passos

- [ ] Melhorar a estilização do site com **CSS** ou framework CSS  
- [ ] Implementar sistema de **registro e login de usuários**  
- [ ] Criar funcionalidade de **salvar builds em banco de dados**  
- [ ] Desenvolver página para **visualizar e pesquisar builds**  

---

## 📷 Demonstração

_(Em breve imagens e gifs mostrando a aplicação em funcionamento)_

---

## 📂 Como Executar o Projeto

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/warframe-build-app.git

# Entre no diretório do projeto
cd warframe-build-app

# Crie e ative o ambiente virtual (opcional)
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Instale as dependências
pip install -r requirements.txt

# Execute o servidor Flask
flask run
