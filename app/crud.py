from sqlalchemy.orm import Session

from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from app.security import gerar_hash_senha


def create_user(db: Session, user: UserCreate):
    senha_hash = gerar_hash_senha(user.senha)

    novo_usuario = User(
        nome=user.nome,
        email=user.email,
        senha=senha_hash
    )

    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)

    return novo_usuario


def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_users(db: Session):
    return db.query(User).all()


def update_user(db: Session, user_id: int, user):
    usuario = db.query(User).filter(User.id == user_id).first()

    if usuario is None:
        return None

    usuario.nome = user.nome
    usuario.email = user.email
    usuario.senha = gerar_hash_senha(user.senha)

    db.commit()
    db.refresh(usuario)

    return usuario


def delete_user(db: Session, user_id: int):
    usuario = db.query(User).filter(User.id == user_id).first()

    if usuario is None:
        return None

    db.delete(usuario)
    db.commit()

    return usuario

def create_task(db: Session, task: TaskCreate, user_id: int):
    nova_task = Task(
        titulo=task.titulo,
        descricao=task.descricao,
        concluida=task.concluida,
        status=task.status,
        prioridade=task.prioridade,
        arquivo=task.arquivo,
        user_id=user_id
    )

    db.add(nova_task)
    db.commit()
    db.refresh(nova_task)

    return nova_task


def get_tasks(db: Session, user_id: int):
    return db.query(Task).filter(Task.user_id == user_id).all()


def get_tasks_by_status(db: Session, status: str, user_id: int):
    return db.query(Task).filter(
        Task.status == status,
        Task.user_id == user_id
    ).all()


def get_task_by_id(db: Session, task_id: int, user_id: int):
    return db.query(Task).filter(
        Task.id == task_id,
        Task.user_id == user_id
    ).first()


def update_task(db: Session, task_id: int, task: TaskUpdate, user_id: int):
    tarefa = db.query(Task).filter(
        Task.id == task_id,
        Task.user_id == user_id
    ).first()

    if tarefa is None:
        return None

    tarefa.titulo = task.titulo
    tarefa.descricao = task.descricao
    tarefa.concluida = task.concluida
    tarefa.status = task.status
    tarefa.prioridade = task.prioridade
    tarefa.arquivo = task.arquivo

    db.commit()
    db.refresh(tarefa)

    return tarefa


def delete_task(db: Session, task_id: int, user_id: int):
    tarefa = db.query(Task).filter(
        Task.id == task_id,
        Task.user_id == user_id
    ).first()

    if tarefa is None:
        return None

    db.delete(tarefa)
    db.commit()

    return tarefa