from datetime import datetime
from typing import Optional


class Task:
    """
    Entidade que representa uma tarefa no sistema.
    """

    def __init__(
        self,
        title: str,
        description: Optional[str] = None,
        task_id: Optional[str] = None,
        completed: bool = False,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
    ):
        """
        Inicializa uma nova tarefa.
        """
        self._validate_title(title)

        self.id = task_id or self._generate_id()
        self.title = title.strip()
        self.description = description.strip() if description else None
        self.completed = completed
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()

    def _validate_title(self, title: str) -> None:
        """
        Valida o título da tarefa.
        """
        if not title or not title.strip():
            raise ValueError("Título da tarefa não pode ser vazio")

        if len(title.strip()) > 200:
            raise ValueError("Título da tarefa deve ter no máximo 200 caracteres")

    def _generate_id(self) -> str:
        """
        Gera um ID único para a tarefa.
        """
        import uuid

        return str(uuid.uuid4())

    def mark_as_completed(self) -> None:
        """
        Marca a tarefa como concluída.
        Atualiza o timestamp de modificação.
        """
        if not self.completed:
            self.completed = True
            self.updated_at = datetime.now()

    def mark_as_pending(self) -> None:
        """
        Marca a tarefa como pendente.
        Atualiza o timestamp de modificação.
        """
        if self.completed:
            self.completed = False
            self.updated_at = datetime.now()

    def update_title(self, new_title: str) -> None:
        """
        Atualiza o título da tarefa.
        """
        self._validate_title(new_title)
        if self.title != new_title.strip():
            self.title = new_title.strip()
            self.updated_at = datetime.now()

    def update_description(self, new_description: Optional[str]) -> None:
        """
        Atualiza a descrição da tarefa.
        """
        processed_description = new_description.strip() if new_description else None
        if self.description != processed_description:
            self.description = processed_description
            self.updated_at = datetime.now()

    def to_dict(self) -> dict:
        """
        Converte a tarefa para um dicionário.
        """
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        """
        Cria uma tarefa a partir de um dicionário.
        """
        return cls(
            title=data["title"],
            description=data.get("description"),
            task_id=data.get("id"),
            completed=data.get("completed", False),
            created_at=datetime.fromisoformat(data["created_at"])
            if data.get("created_at")
            else None,
            updated_at=datetime.fromisoformat(data["updated_at"])
            if data.get("updated_at")
            else None,
        )

    def __eq__(self, other) -> bool:
        """
        Compara duas tarefas por igualdade.
        """
        if not isinstance(other, Task):
            return False
        return self.id == other.id
