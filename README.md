# CloudTask-AI

API de gerenciamento de tarefas desenvolvida com **FastAPI**, **PostgreSQL**, **Docker** e **Kubernetes**, com autenticação via **JWT**, CRUD de tarefas, filtro por status e suporte a upload de arquivos.

---

## Integrantes

* João Gabriel RU: 5327853
* Izabela Xavier RU: 5315281

---

## Objetivo do projeto

O projeto **CloudTask-AI** foi desenvolvido com o objetivo de criar uma API REST para gerenciamento de tarefas, permitindo o cadastro e autenticação de usuários, criação e organização de tarefas e testes de deploy com containers e Kubernetes.

A aplicação foi construída com foco em práticas modernas de backend, utilizando:

* **FastAPI** para criação da API
* **PostgreSQL** como banco de dados
* **SQLAlchemy** como ORM
* **JWT** para autenticação
* **Docker** para containerização
* **Kubernetes** para orquestração da aplicação

---

# Funcionalidades

## Usuários

* Cadastro de usuário
* Login com geração de token JWT
* Autenticação para acesso às rotas protegidas

## Tarefas

* Criar tarefa
* Listar tarefas do usuário autenticado
* Buscar tarefa por ID
* Atualizar tarefa
* Excluir tarefa
* Filtrar tarefas por status

## Extras implementados

* Campo de **prioridade**
* Campo de **status**
* Upload de arquivos
* Documentação automática via Swagger

---

# Tecnologias utilizadas

* Python 3.11
* FastAPI
* Uvicorn
* SQLAlchemy
* PostgreSQL
* Pydantic
* Passlib / bcrypt
* Python-Jose
* Docker
* Docker Compose
* Kubernetes
* Git / GitHub

---

# Estrutura do projeto

```bash
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
│   ├── Dockerfile
│   ├── docker-compose.yml
│   └── requirements.txt
│
└── README.md
```

---

# Como executar o projeto localmente

## 1. Clonar o repositório

```bash
git clone <chttps://github.com/jgcosta7/CloudTask-AI>
cd CloudTask-AI/backend
```

## 2. Criar e ativar o ambiente virtual

### Windows (PowerShell)

```bash
python -m venv venv
.\venv\Scripts\activate
```

## 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

## 4. Rodar a aplicação

```bash
uvicorn app.main:app --reload
```

## 5. Acessar no navegador

* Swagger: `http://localhost:8000/docs`

---

# Como executar com Docker

## 1. Na pasta `backend`, rodar:

```bash
docker compose up --build
```

## 2. Acessar no navegador

* Swagger: `http://localhost:8000/docs`

---

# Como executar com Kubernetes

## Pré-requisito

Ter o **Docker Desktop** instalado com o **Kubernetes habilitado**.

## 1. Entrar na pasta do backend

```bash
cd backend
```

## 2. Verificar se o Kubernetes está ativo

```bash
kubectl get nodes
```

## 3. Aplicar o deployment da API

```bash
kubectl apply -f k8s/api-deployment.yaml
```

## 4. Verificar se o pod está rodando

```bash
kubectl get pods
```

## 5. Aplicar o service

```bash
kubectl apply -f k8s/api-service.yaml
```

## 6. Criar o port-forward para acessar a API

```bash
kubectl port-forward service/cloudtask-api-service 8000:8000
```

## 7. Acessar a documentação

* Swagger: `http://localhost:8000/docs`

---

# Autenticação

A autenticação da API é feita via **JWT**.

## Fluxo básico:

1. Criar usuário em `/users/`
2. Fazer login em `/login`
3. Copiar o token retornado
4. Clicar em **Authorize** no Swagger
5. Informar o token no formato:

```bash
Bearer SEU_TOKEN
```

---

# Principais endpoints

## Usuários

* `POST /users/` → criar usuário
* `POST /login` → autenticar usuário

## Tarefas

* `GET /tasks/` → listar tarefas
* `GET /tasks/{task_id}` → buscar tarefa por ID
* `POST /tasks/` → criar tarefa
* `PUT /tasks/{task_id}` → atualizar tarefa
* `DELETE /tasks/{task_id}` → excluir tarefa
* `GET /tasks/status/{status}` → listar tarefas por status

## Upload

* rota de upload implementada no projeto

---

# Exemplo de JSON para criar tarefa

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

# Exemplo de retorno de tarefa

```json
{
  "id": 1,
  "titulo": "Estudar Kubernetes",
  "descricao": "Criar manifests do projeto",
  "concluida": false,
  "status": "pendente",
  "prioridade": "alta",
  "user_id": 1
}
```

---

# Evidências de funcionamento

Durante o desenvolvimento, foram realizados testes de:

* cadastro de usuário
* login com JWT
* criação de tarefas
* atualização de tarefas
* filtro por status
* execução com Docker
* execução com Kubernetes
* acesso à documentação Swagger

---

# Considerações finais

O projeto permitiu aplicar conhecimentos de desenvolvimento backend, autenticação, integração com banco de dados, containerização e orquestração com Kubernetes, simulando um ambiente mais próximo de aplicações modernas em nuvem.