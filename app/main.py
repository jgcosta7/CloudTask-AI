from fastapi import FastAPI
from app.database import engine, Base
from app.models.user import User
from app.models.task import Task
from app.routes.user import router as user_router
from app.routes.task import router as task_router

app = FastAPI(
    title="CloudTask AI",
    description="API de gerenciamento de tarefas",
    version="1.0.0"
)

# Cria todas as tabelas cadastradas no projeto
Base.metadata.create_all(bind=engine)

# Rotas
app.include_router(user_router)
app.include_router(task_router)


@app.get("/", tags=["Sistema"])
def home():
    return {
        "mensagem": "Bem-vindo ao CloudTask AI!"
    }


@app.get("/status", tags=["Sistema"])
def status():
    return {
        "status": "API funcionando"
    }