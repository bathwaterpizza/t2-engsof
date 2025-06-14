from typing import List, Optional, Dict
from ..domain.task import Task
from ..domain.task_database import TaskDatabase


class DictTaskDatabase(TaskDatabase):
    """Implementação em memória do repositório de tarefas, simulando um BD"""

    def __init__(self):
        self._tasks: Dict[str, Task] = {}

    def save(self, task: Task) -> Task:
        """Salva uma tarefa"""
        self._tasks[task.id] = task
        return task

    def find_by_id(self, task_id: str) -> Optional[Task]:
        """Busca uma tarefa por ID"""
        return self._tasks.get(task_id)

    def find_all(self) -> List[Task]:
        """Busca todas as tarefas"""
        return list(self._tasks.values())

    def update(self, task: Task) -> Task:
        """Atualiza uma tarefa"""
        if task.id in self._tasks:
            self._tasks[task.id] = task
        return task

    def delete_by_id(self, task_id: str) -> bool:
        """Remove uma tarefa por ID"""
        if task_id in self._tasks:
            del self._tasks[task_id]
            return True
        return False

    def count_all(self) -> int:
        """Conta o total de tarefas"""
        return len(self._tasks)
