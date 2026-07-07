from pydantic import BaseModel


class TaskBase(BaseModel):
    titulo: str
    descricao: str | None = None
    concluida: bool = False
    status: str = "pendente"
    prioridade: str = "media"
    arquivo: str | None = None


class TaskCreate(TaskBase):
    pass


class TaskUpdate(TaskBase):
    pass


class TaskResponse(TaskBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True