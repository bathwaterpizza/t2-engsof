from typing import Optional
from ..domain.task import Task
from ..domain.database import Database
from ..domain.exceptions import TaskNotFoundError


class UpdateTaskUseCase:
    """Caso de uso para atualizar uma tarefa"""

    def __init__(self, task_repository: Database[Task]):
        self._task_repository = task_repository

    def execute(
        self,
        task_id: str,
        title: Optional[str] = None,
        description: Optional[str] = None,
        completed: Optional[bool] = None,
    ) -> Task:
        """Executa a atualização de uma tarefa"""
        task = self._task_repository.find_by_id(task_id)
        if not task:
            raise TaskNotFoundError(f"Tarefa com ID {task_id} não encontrada")

        if title is not None:
            task.update_title(title)

        if description is not None:
            task.update_description(description)

        if completed is not None:
            if completed:
                task.mark_as_completed()
            else:
                task.mark_as_pending()

        return self._task_repository.update(task)
