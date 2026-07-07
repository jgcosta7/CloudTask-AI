from typing import List

from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.task import TaskCreate, TaskUpdate, TaskResponse
from app.crud import (
    create_task,
    get_tasks,
    get_task_by_id,
    update_task,
    delete_task,
    get_tasks_by_status
)
from app.security import get_current_user

import os

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@router.get("/", response_model=List[TaskResponse])
def listar_tasks(
    db: Session = Depends(get_db),
    usuario=Depends(get_current_user)
):
    return get_tasks(db, usuario.id)


@router.get("/status/{status}", response_model=List[TaskResponse])
def listar_tasks_por_status(
    status: str,
    db: Session = Depends(get_db),
    usuario=Depends(get_current_user)
):
    return get_tasks_by_status(db, status, usuario.id)


@router.get("/{task_id}", response_model=TaskResponse)
def buscar_task(
    task_id: int,
    db: Session = Depends(get_db),
    usuario=Depends(get_current_user)
):
    tarefa = get_task_by_id(db, task_id, usuario.id)

    if tarefa is None:
        raise HTTPException(
            status_code=404,
            detail="Task não encontrada"
        )

    return tarefa


@router.post("/", response_model=TaskResponse)
def criar_task(
    task: TaskCreate,
    db: Session = Depends(get_db),
    usuario=Depends(get_current_user)
):
    return create_task(db, task, usuario.id)


@router.put("/{task_id}", response_model=TaskResponse)
def atualizar_task(
    task_id: int,
    task: TaskUpdate,
    db: Session = Depends(get_db),
    usuario=Depends(get_current_user)
):
    tarefa = update_task(db, task_id, task, usuario.id)

    if tarefa is None:
        raise HTTPException(
            status_code=404,
            detail="Task não encontrada"
        )

    return tarefa


@router.post("/{task_id}/upload")
def upload_arquivo_task(
    task_id: int,
    arquivo: UploadFile = File(...),
    db: Session = Depends(get_db),
    usuario=Depends(get_current_user)
):
    tarefa = get_task_by_id(db, task_id, usuario.id)

    if tarefa is None:
        raise HTTPException(
            status_code=404,
            detail="Task não encontrada"
        )

    os.makedirs("uploads", exist_ok=True)

    caminho_arquivo = f"uploads/{arquivo.filename}"

    with open(caminho_arquivo, "wb") as buffer:
        buffer.write(arquivo.file.read())

    tarefa.arquivo = caminho_arquivo
    db.commit()
    db.refresh(tarefa)

    return {
        "mensagem": "Arquivo enviado com sucesso",
        "arquivo": caminho_arquivo
    }


@router.delete("/{task_id}")
def excluir_task(
    task_id: int,
    db: Session = Depends(get_db),
    usuario=Depends(get_current_user)
):
    tarefa = delete_task(db, task_id, usuario.id)

    if tarefa is None:
        raise HTTPException(
            status_code=404,
            detail="Task não encontrada"
        )

    return {"mensagem": "Task excluída com sucesso"}