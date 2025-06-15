from src.domain.task import Task
from ..domain.database import Database
from ..domain.exceptions import TaskNotFoundError


class DeleteTaskUseCase:
    """Caso de uso para deletar uma tarefa"""

    def __init__(self, task_repository: Database[Task]):
        self._task_repository = task_repository

    def execute(self, task_id: str) -> bool:
        """Executa a remoção de uma tarefa"""
        task = self._task_repository.find_by_id(task_id)
        if not task:
            raise TaskNotFoundError(f"Tarefa com ID {task_id} não encontrada")

        return self._task_repository.delete_by_id(task_id)
