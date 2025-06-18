from typing import Optional
from ..domain.task import Task
from ..domain.database import Database


class CreateTaskUseCase:
    """Caso de uso para criar uma nova tarefa"""

    def __init__(self, task_repository: Database[Task]):
        self._task_repository = task_repository

    def execute(
        self,
        title: str,
        description: Optional[str] = None,
        category_id: Optional[str] = None,
    ) -> Task:
        """Executa a criação de uma nova tarefa"""
        task = Task(title=title, description=description, category_id=category_id)
        return self._task_repository.save(task)
