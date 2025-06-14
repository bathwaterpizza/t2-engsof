from typing import Optional
from ..domain.task import Task
from ..domain.task_database import TaskDatabase


class CreateTaskUseCase:
    """Caso de uso para criar uma nova tarefa"""

    def __init__(self, task_repository: TaskDatabase):
        self._task_repository = task_repository

    def execute(self, title: str, description: Optional[str] = None) -> Task:
        """Executa a criação de uma nova tarefa"""
        task = Task(title=title, description=description)
        return self._task_repository.save(task)
