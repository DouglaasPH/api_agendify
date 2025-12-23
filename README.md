# 🧩 Backend — Agendify API

O **Agendify Backend** é uma API desenvolvida em **FastAPI** para gerenciar toda a lógica do sistema de agendamento, incluindo autenticação completa, gerenciamento de usuários, disponibilidade, agendamentos e chat entre cliente e profissional.
O projeto segue boas práticas de arquitetura, versionamento de banco, segurança e envio de e-mails.

---

## 🚀 Tecnologias Utilizadas

* **FastAPI** — Framework principal
* **Uvicorn** — Servidor ASGI
* **SQLAlchemy** — ORM
* **Alembic** — Migrações de banco
* **JWT Authentication (python-jose)** — Segurança
* **Fastapi-Mail** — Envio de e-mails transacionais
* **Jinja2** — Templates de e-mail
* **SQLite** (desenvolvimento)
* **Poetry** — Gerenciamento de dependências via `pyproject.toml`

---

## 📁 Estrutura do Projeto

```
backend/

├── src/
│   ├── alembic/           # Migrações do banco
│   ├── controllers/       # Rotas (camada de controle)
│   ├── models/            # Modelos ORM (SQLAlchemy)
│   ├── schemas/           # Schemas Pydantic
│   ├── services/          # Funções de lógica e regras de negócio usadas pelas rotas
│   ├── templates/         # Templates Jinja2 (e-mails)
│   ├── views/             # Objetos simples de request/response usados nas rotas
│   └── main.py            # Inicialização da aplicação FastAPI
│   └── alembic.ini               # Configurações do Alembic
│   └── database.py               # Conexão e sessão com o banco
│   └── mail_config.py            # Configuração de e-mails (Fastapi-Mail)
│   └── main.py                   # Ponto principal de inicialização (caso execute pela raiz)
├── pyproject.toml            # Dependências (Poetry)
```

---

## 🧠 Arquitetura Explicada

controllers/
Contêm as rotas.
Recebem a requisição → chamam serviços → retornam respostas.

services/
Funções com lógica de negócio reutilizável, usadas pelos controllers.
Ex.: criação de usuário, validação de horários, regras de agendamento, envio de e-mail, etc.

models/
Representação das tabelas do banco com SQLAlchemy.

schemas/
Estruturas completas de entrada/saída (Pydantic) vinculadas a entidades.
Ex.: UserCreate, AppointmentOut, ScheduleBase.

views/
Payloads simples usados diretamente nas rotas.
Exemplo real:
```
class UserEmailToUpdate(BaseModel):
    new_email: str
```
Servem como tipos específicos para operações muito objetivas.

templates/
HTML de e-mails enviados pelo sistema.

database.py
Gerencia a conexão e sessão com o banco.

mail_config.py
Configura SMTP, usuários, templates e envio via Fastapi-Mail.

alembic/
Gerencia migrações (upgrade/downgrade).


---

# ✨ Funcionalidades da API

## 👤 **Autenticação e Usuários**

* Registro com envio de e-mail de confirmação
* Login com **access_token** e **refresh_token**
* Recuperação de senha (Forgot + Reset) com e-mail
* Alteração de e-mail com validação e envio de confirmação
* Edição de perfil
* Autorização por níveis

---

## 📅 **Disponibilidade**

* Criar horários disponíveis
* Remover horários
* Listagem de horários por profissional

---

## 🗓️ **Agendamentos**

* Cliente agenda um horário
* Cliente cancela um agendamento
* Profissional visualiza agendamentos de todos os clientes
* Validação contra conflitos

---

## 💬 **Chat Integrado**

* Chat exclusivo para cada profissional
* Mensagens baseadas em código único
* Fluxo de: agendar, desmarcar e listar horários

---

## 📊 **Métricas**

* Quantidade de agendamentos
* Cancelamentos
* Visão geral para o profissional

---

# ⚙️ Como Executar o Backend

## 1️⃣ Entrar na pasta do backend

```
cd backend
```

---

## 2️⃣ Instalar dependências (Poetry)

```
poetry install
```

---

## 3️⃣ Ativar o ambiente virtual

```
poetry shell
```

---

## 4️⃣ Rodar migrações do Alembic

```
alembic upgrade head
```

---

## 5️⃣ Iniciar o servidor

```
uvicorn app.main:app --reload
```

API disponível em:
👉 [http://localhost:8000](http://localhost:8000)
Documentação automática:
👉 [http://localhost:8000/docs](http://localhost:8000/docs)
👉 [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

# 📨 E-mails

Este backend envia e-mails usando:

* **Fastapi-Mail**
* **Jinja2 templates**

Fluxos que usam e-mail:

* Registro
* Login
* Alteração de e-mail
* Esqueci a senha
* Redefinição de senha

---

# 🔐 Segurança

* Tokens JWT (access + refresh)
* Rotas protegidas com dependências
* Tokens de redefinição seguros
* Revogação automática em fluxos sensíveis
