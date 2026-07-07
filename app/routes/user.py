from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from app.database import get_db
from app.schemas.user import (
    UserCreate,
    UserUpdate,
    UserResponse,
    Token
)
from app.crud import (
    create_user,
    get_user_by_id,
    get_user_by_email,
    get_users,
    update_user,
    delete_user
)
from app.security import verificar_senha, criar_access_token, get_current_user

router = APIRouter(
    prefix="/users",
    tags=["Usuários"]
)


@router.get("/", response_model=List[UserResponse])
def listar_usuarios(db: Session = Depends(get_db)):
    return get_users(db)


@router.post("/", response_model=UserResponse)
def criar_usuario(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)


@router.post("/login", response_model=Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    usuario = get_user_by_email(db, form_data.username)

    if usuario is None:
        raise HTTPException(
            status_code=401,
            detail="Email ou senha inválidos"
        )

    senha_valida = verificar_senha(form_data.password, usuario.senha)

    if not senha_valida:
        raise HTTPException(
            status_code=401,
            detail="Email ou senha inválidos"
        )

    access_token = criar_access_token(
        data={
            "sub": str(usuario.id),
            "email": usuario.email
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


@router.get("/me", response_model=UserResponse)
def ler_meu_usuario(usuario=Depends(get_current_user)):
    return usuario


@router.get("/{user_id}", response_model=UserResponse)
def buscar_usuario(user_id: int, db: Session = Depends(get_db)):
    usuario = get_user_by_id(db, user_id)

    if usuario is None:
        raise HTTPException(
            status_code=404,
            detail="Usuário não encontrado"
        )

    return usuario


@router.put("/{user_id}", response_model=UserResponse)
def atualizar_usuario(
    user_id: int,
    user: UserUpdate,
    db: Session = Depends(get_db)
):
    usuario = update_user(db, user_id, user)

    if usuario is None:
        raise HTTPException(
            status_code=404,
            detail="Usuário não encontrado"
        )

    return usuario


@router.delete("/{user_id}")
def excluir_usuario(
    user_id: int,
    db: Session = Depends(get_db)
):
    usuario = delete_user(db, user_id)

    if usuario is None:
        raise HTTPException(
            status_code=404,
            detail="Usuário não encontrado"
        )

    return {
        "mensagem": "Usuário excluído com sucesso"
    }