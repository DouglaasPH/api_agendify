# 🧩 API Agendify

API REST para gerenciamento de agendamentos, profissionais, clientes e autenticação, desenvolvida com **FastAPI**, **SQLAlchemy**, **PostgreSQL** e **Docker**.

<br>

## 🚀 Tecnologias Utilizadas

- **Python 3.11** - Linguagem de programação do projeto
- **FastAPI** — Framework moderno e rápido
- **Uvicorn** — Servidor ASGI de alto desempenho para executar a aplicação FASTAPI
- **SQLAlchemy** — ORM para mapeamento objeto-relacional e gerenciamento do banco de dados
- **PostgreSQL 16** — Banco de dados relacional
- **JWT (python-jose)** — Implementação de tokens JWT para autenticação e segurança
- **Passlib (bcrypt)** — Biblioteca para hashing seguro de senhas
- **Fastapi-Mail** — Envio de e-mails diretamente pela aplicação
- **Jinja2** — Motor de templates para criação de e-mails dinâmicos
- **Pydantic v2** - Validação e modelagem de dados de forma segura e eficiente
- **Poetry** — Gerenciamento de dependências e ambientes via `pyproject.toml`
- **Black & Flake8** - Ferramenta de formatação de código e linting para manter a qualidade do código

<br>

## 📁 Estrutura do Projeto

```
api_agendify/
├─── db/
│    └── init.sql
├─── src/
│    ├── application/
│    │   ├── schemas/
│    │   │   ├── appointment.py
│    │   │   ├── availability.py
│    │   │   ├── customer.py
│    │   │   └── professional.py
│    │   └── use_cases/
│    │       ├── appointment/
│    │       │   ├── cancel_appointment.py
│    │       │   ├── create_appointment.py
│    │       │   ├── get_by_id_appointment.py
│    │       │   └── list_appointment.py
│    │       ├── auth/
│    │       │   ├── generate_verification_token.py
│    │       │   └── refresh_token.py
│    │       ├── availability/
│    │       │   ├── create_availability.py
│    │       │   ├── delete_availability.py
│    │       │   ├── get_by_id_availability.py
│    │       │   └── list_availability.py
│    │       ├── customer/
│    │       │   ├── login_by_id_customer.py
│    │       │   └── register_customer.py
│    │       └── professional/
│    │           ├── check_professional_email.py
│    │           ├── confirm_email_change_for_professional.py
│    │           ├── delete_professional.py
│    │           ├── generate_register_verification_professional.py
│    │           ├── get_professional.py
│    │           ├── login_professional.py
│    │           ├── logout_professional.py
│    │           ├── register_professional.py
│    │           ├── request_password_for_professional.py
│    │           ├── reset_password_for_professional.py
│    │           ├── send_email_to_change_email_for_professional.py
│    │           └── update_professional_profile.py
│    ├── domain/
│    │   ├── entities/
│    │   │   ├── appointment.py
│    │   │   ├── availability.py
│    │   │   ├── customer.py
│    │   │   └── professional.py
│    │   ├── repositories/
│    │   │   ├── appointment_repository.py
│    │   │   ├── availability_repository.py
│    │   │   ├── customer_repository.py
│    │   │   └── professional_repository.py
│    │   └── services/
│    │       └── email_service.py
│    ├── infrastructure/
│    │   ├── database/
│    │   │   ├── models/
│    │   │   │   ├── appointment.py
│    │   │   │   ├── availability.py
│    │   │   │   ├── customer.py
│    │   │   │   ├── professional.py
│    │   │   │   └── refresh_token.py
│    │   │   ├── repositories/
│    │   │   │   ├── appointment_repository.py
│    │   │   │   ├── availability_repository.py
│    │   │   │   ├── customer_repository.py
│    │   │   │   ├── professional_repository.py
│    │   │   │   └── refresh_token_repository.py
│    │   │   ├── base.py
│    │   │   └── session.py
│    │   ├── email/
│    │   │   ├── templates/
│    │   │   │   ├── email_change_confirmation.html
│    │   │   │   ├── login_email.html
│    │   │   │   ├── password_reset_email.html
│    │   │   │   ├── verification_email.html
│    │   │   │   └── welcome_email.html
│    │   │   ├── fastapi_mail_service.py
│    │   │   └── mail_config.py
│    │   ├── security/
│    │   │   ├── password_hasher.py
│    │   │   └── token_service.py
│    │   └── settings.py
│    ├── presentation/
│    │   ├── controllers/
│    │   │   ├── appointment_controller.py
│    │   │   ├── availability_controller.py
│    │   │   ├── customer_controller.py
│    │   │   ├── professional_controller.py
│    │   │   └── refresh_token_controller.py
│    │   └── dependencies/
│    │       ├── appointment.py
│    │       ├── auth.py
│    │       ├── availability.py
│    │       ├── customer.py
│    │       ├── database.py
│    │       ├── email.py
│    │       └── professional.py
│    ├── main.py
│    └── database.py
├── .env.example
├──  .gitignore
├── docker-compose.yml
├── Dockerfile
├── poetry.lock
├── pyproject.toml
└── README.md
```

<br>

## 🧠 Arquitetura Explicada

<br>

## Rotas

| Método   | Rota                                                  | Descrição                                                         |
| -------- | ----------------------------------------------------- | ----------------------------------------------------------------- |
| **POST** | `/refresh-token`                                      | atualizar access_token                                            |
| **GET**  | `/professional/check-email`                           | Verificar email                                                   |
| **GET**  | `/professional`                                       | Obter dados do profissional pelo ID profissional do access_token  |
| **GET**  | `/professional/{chat_code}`                           | Obter dados do profissional pelo chat_code para clientes          |
| **PUT**  | `/professional/modify-data`                           | Modificar dados do profissional                                   |
| **POST** | `/professional/send-email-to-change-email`            | Enviar email para mudança de email (autorização)                  |
| **POST** | `/professional/send-email-to-change-password`         | Enviar email para mudança de senha (autorização)                  |
| **PUT**  | `/professional/confirm-email-modification`            | Confirmar modificação de email (autorização)                      |
| **PUT**  | `/professional/confirm-password-modification`         | Confirmar modificação de senha (autorização)                      |
| **POST** | `/professional/login`                                 | Login                                                             |
| **POST** | `/professional/generate-verification-token`           | Gerar token para confimar criação de conta no email (autorização) |
| **POST** | `/professional/register`                              | Registrar conta                                                   |
| **POST** | `/customer/login/{customer_id}`                       | Login através do customer_id                                      |
| **POST** | `/customers/`                                         | Registrar, se tiver conta faça login                              |
| **POST** | `/availability/professional/create`                   | Criar disponibilidade por meio do profissional                    |
| **GET**  | `/availability/professional/{availability_id}`        | Pegar disponibilidade para profissional                           |
| **GET**  | `/availability/professional/list`                     | Listar disponibilidade para profissional                          |
| **GET**  | `/availability/customer/list`                         | Listar disponibilidade para cliente                               |
| **PUT**  | `/availability/professional/delete/{availability_id}` | Deletar disponibilidade por meio do profissional                  |
| **POST** | `/appointment/customer/create`                        | Criar agendamento por meio do cliente                             |
| **GET**  | `/appointment/customer/cancel/{appointment_id}`       | Cancelar agendamento por meio do cliente                          |
| **GET**  | `/appointment/professional/cancel/{appointment_id}`   | Cancelar agendamento por meio do profissional                     |
| **GET**  | `/appointment/customer/list`                          | Listar agendamentos do profissional para o cliente                |
| **GET**  | `/appointment/professional/list`                      | Listar agendamentos do profissional para o profissional           |
| **PUT**  | `/appointment/professional/get/{appointment_id}`      | Pegar agendamento do profissional para o profissional             |

<br>

## ⚙️ Pré-requisitos

- **Docker**
- **Docker Compose**
- **Não é necessário instalar Python ou PostgreSQL localmente**

<br>

## ⚙️ Variáveis de Ambiente (**.env**)

Crie um arquivo **.env** na raiz do projeto:

```env
# Database
DATABASE_URL=postgresql://root_agendify:rootpassword@db:5432/agendify

# Security
SECRET_KEY=supersecretkey
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_EXPIRE_DAYS=7

# Frontend
FRONTEND_BASE_URL=http://localhost:3000

# Email
MAIL_USERNAME=example@gmail.com
MAIL_PASSWORD=your_password
MAIL_FROM=example@gmail.com
MAIL_PORT=587
MAIL_SERVER=smtp.gmail.com
MAIL_STARTTLS=true
MAIL_SSL_TLS=false
USE_CREDENTIALS=true
TEMPLATE_FOLDER=templates

```

<br>

## 🐳 Docker

Subir a aplicação + banco de dados

```bash
docker compose up --build
```

A API ficará disponível em:

```
http://localhost:8000

```

<br>

## 📘 Documentação da API

- Swagger UI
  <br>
  👉 http://localhost:8000/docs

<br>

## 🗄️ Banco de Dados

- PostgreSQL 16
- Inicializado automaticamente via init.sql
- Persistência via volume Docker

### Acessar o banco dentro do container:

```bash
docker exec -it agendify_db psql -U root_agendify agendify
```

<br>

## 🧪 Qualidade de Código

### Black

```bash
black .
```

### Flake8

```bash
flake8 .
```

<br>

## 🔐 Autenticação

- JWT Access Token
- Refresh Token
- Hash de senha com bcrypt
- Fluxo de verificação de cadastro por e-mail

<br>

## ✉️ Email

- Envio de e-mails usando FastAPI-Mail
- Templates com _Jinja2_
- Configuração via **.env**

<br>

## 🧠 Arquitetura

O projeto segue princípios de:

- Clean Architecture
- Separation of Concerns
- Dependency Inversion
- Domain-driven design (DDD simplificado)

<br>

## 👨‍💻 Autor

### Douglas Phelipe

douglasphelipedpss@gmail.com
