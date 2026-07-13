# CloudTask-AI

API de gerenciamento de tarefas desenvolvida com **FastAPI**, **PostgreSQL**, **Docker** e **Kubernetes**, utilizando autenticação via **JWT**, CRUD completo de tarefas, filtro por status e upload de arquivos.

---

# Integrantes

- **João Gabriel Costa Fernando** — RU: 5327853
- **Izabela Xavier** — RU: 5315281

---

# Objetivo do projeto

O **CloudTask-AI** foi desenvolvido como uma API REST para gerenciamento de tarefas, permitindo o cadastro e autenticação de usuários, criação e organização de tarefas, upload de arquivos e implantação da aplicação utilizando Docker e Kubernetes.

A aplicação foi construída utilizando:

- FastAPI
- PostgreSQL
- SQLAlchemy
- JWT (JSON Web Token)
- Docker
- Kubernetes

---

# Funcionalidades

## Usuários

- Cadastro de usuários
- Login com JWT
- Consulta do usuário autenticado
- Atualização de usuário
- Exclusão de usuário

## Tarefas

- Criar tarefa
- Listar tarefas
- Buscar tarefa por ID
- Atualizar tarefa
- Excluir tarefa
- Filtrar tarefas por status

## Recursos adicionais

- Upload de arquivos para tarefas
- Campo de prioridade
- Campo de status
- Documentação automática via Swagger

---

# Tecnologias utilizadas

- Python 3.11
- FastAPI
- Uvicorn
- SQLAlchemy
- PostgreSQL
- Pydantic
- Passlib
- bcrypt
- python-jose
- Docker
- Docker Compose
- Kubernetes
- Git
- GitHub

---

# Estrutura do projeto

```text
CloudTask-AI/
│
├── backend/
│   ├── app/
│   │   ├── models/
│   │   ├── routes/
│   │   ├── schemas/
│   │   ├── database.py
│   │   ├── crud.py
│   │   ├── security.py
│   │   └── main.py
│   │
│   ├── k8s/
│   │   ├── api-deployment.yaml
│   │   └── api-service.yaml
│   │
│   ├── uploads/
│   ├── Dockerfile
│   ├── docker-compose.yml
│   ├── requirements.txt
│   └── README.md
│
└── docs/
```

---

# Como executar o projeto localmente

## 1. Clonar o repositório

```bash
git clone https://github.com/jgcosta7/CloudTask-AI.git
cd CloudTask-AI/backend
```

---

## 2. Criar o ambiente virtual

### Windows

```bash
python -m venv venv
.\venv\Scripts\activate
```

### Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

---

## 4. Configurar o banco de dados

Crie um banco PostgreSQL chamado:

```
cloudtask_ai
```

Configure a conexão no arquivo **app/database.py** ou utilize a variável de ambiente:

```
DATABASE_URL=postgresql://usuario:senha@localhost:5432/cloudtask_ai
```

---

## 5. Executar a aplicação

```bash
uvicorn app.main:app --reload
```

Na primeira execução, todas as tabelas serão criadas automaticamente pelo SQLAlchemy.

> **Observação:** Caso o banco já exista e o modelo das tabelas seja alterado durante o desenvolvimento, poderá ser necessário recriar a tabela correspondente para atualizar sua estrutura.

---

## 6. Acessar a documentação

Swagger:

```
http://localhost:8000/docs
```

---

# Executando com Docker

Na pasta **backend**, execute:

```bash
docker compose up --build
```

Depois acesse:

```
http://localhost:8000/docs
```

---

# Executando com Kubernetes

### Pré-requisitos

- Docker Desktop
- Kubernetes habilitado

---

Aplicar os manifests:

```bash
kubectl apply -f k8s/api-deployment.yaml
kubectl apply -f k8s/api-service.yaml
```

Verificar os pods:

```bash
kubectl get pods
```

Verificar os serviços:

```bash
kubectl get services
```

Criar o port-forward:

```bash
kubectl port-forward service/cloudtask-api-service 8000:8000
```

Acessar:

```
http://localhost:8000/docs
```

---

# Autenticação

Fluxo de utilização:

1. Criar um usuário.
2. Fazer login.
3. Copiar o token JWT retornado.
4. Clicar em **Authorize** no Swagger.
5. Informar:

```
Bearer SEU_TOKEN
```

---

# Principais endpoints

## Sistema

| Método | Endpoint | Descrição |
|---------|----------|-----------|
| GET | `/` | Página inicial da API |
| GET | `/status` | Verifica o funcionamento da API |

---

## Usuários

| Método | Endpoint | Descrição |
|---------|----------|-----------|
| GET | `/users/` | Listar usuários |
| POST | `/users/` | Criar usuário |
| POST | `/users/login` | Realizar login |
| GET | `/users/me` | Retorna o usuário autenticado |
| GET | `/users/{user_id}` | Buscar usuário por ID |
| PUT | `/users/{user_id}` | Atualizar usuário |
| DELETE | `/users/{user_id}` | Excluir usuário |

---

## Tarefas

| Método | Endpoint | Descrição |
|---------|----------|-----------|
| GET | `/tasks/` | Listar tarefas |
| POST | `/tasks/` | Criar tarefa |
| GET | `/tasks/status/{status}` | Filtrar tarefas por status |
| GET | `/tasks/{task_id}` | Buscar tarefa por ID |
| PUT | `/tasks/{task_id}` | Atualizar tarefa |
| DELETE | `/tasks/{task_id}` | Excluir tarefa |
| POST | `/tasks/{task_id}/upload` | Upload de arquivo da tarefa |

---

# Exemplo de criação de tarefa

```json
{
  "titulo": "Estudar Kubernetes",
  "descricao": "Criar manifests do projeto",
  "concluida": false,
  "status": "pendente",
  "prioridade": "alta"
}
```

---

# Exemplo de resposta

```json
{
  "id": 1,
  "titulo": "Estudar Kubernetes",
  "descricao": "Criar manifests do projeto",
  "concluida": false,
  "status": "pendente",
  "prioridade": "alta",
  "arquivo": null,
  "user_id": 1
}
```

---

# Evidências de funcionamento

Foram realizados testes das seguintes funcionalidades:

- Cadastro de usuários
- Login com JWT
- CRUD completo de tarefas
- Consulta de tarefas por status
- Upload de arquivos
- Documentação Swagger
- Execução utilizando Docker
- Execução utilizando Kubernetes

---

# Considerações finais

O desenvolvimento do **CloudTask-AI** possibilitou aplicar conceitos de desenvolvimento de APIs REST, autenticação com JWT, persistência de dados utilizando PostgreSQL, containerização com Docker e orquestração com Kubernetes.

O projeto integra tecnologias amplamente utilizadas no mercado e serve como uma base para aplicações modernas voltadas ao gerenciamento de tarefas em ambientes de computação em nuvem.