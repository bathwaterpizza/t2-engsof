from typing import List
from ..domain.task import Task
from ..domain.task_database import TaskDatabase


class GetAllTasksUseCase:
    """Caso de uso para buscar todas as tarefas"""

    def __init__(self, task_repository: TaskDatabase):
        self._task_repository = task_repository

    def execute(self) -> List[Task]:
        """Executa a busca de todas as tarefas"""
        return self._task_repository.find_all()
