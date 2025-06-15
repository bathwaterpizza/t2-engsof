from typing import Optional, List
from .task import Task


class Category:
    """Entidade que representa uma categoria de tarefas."""

    def __init__(
        self,
        name: str,
        description: Optional[str] = None,
        category_id: Optional[str] = None,
    ):
        self._validate_name(name)
        self.id = category_id or self._generate_id()
        self.name = name.strip()
        self.description = description.strip() if description else None
        self.tasks: List[Task] = []

    def _validate_name(self, name: str) -> None:
        if not name or not name.strip():
            raise ValueError("Nome da categoria não pode ser vazio")
        if len(name.strip()) > 100:
            raise ValueError("Nome da categoria deve ter no máximo 100 caracteres")

    def _generate_id(self) -> str:
        import uuid

        return str(uuid.uuid4())

    def add_task(self, task: Task) -> None:
        if task not in self.tasks:
            self.tasks.append(task)

    def remove_task(self, task: Task) -> None:
        if task in self.tasks:
            self.tasks.remove(task)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "tasks": [task.id for task in self.tasks],
        }

    @classmethod
    def from_dict(cls, data: dict, tasks_lookup: Optional[dict] = None) -> "Category":
        cat = cls(
            name=data["name"],
            description=data.get("description"),
            category_id=data.get("id"),
        )
        if tasks_lookup and "tasks" in data:
            for task_id in data["tasks"]:
                if task_id in tasks_lookup:
                    cat.add_task(tasks_lookup[task_id])
        return cat

    def __eq__(self, other) -> bool:
        if not isinstance(other, Category):
            return False
        return self.id == other.id
