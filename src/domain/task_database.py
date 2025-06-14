from abc import ABC, abstractmethod
from typing import List, Optional
from .task import Task


class TaskDatabase(ABC):
    """Interface para repositório de tarefas"""

    @abstractmethod
    def save(self, task: Task) -> Task:
        """Salva uma tarefa"""
        pass

    @abstractmethod
    def find_by_id(self, task_id: str) -> Optional[Task]:
        """Busca uma tarefa por ID"""
        pass

    @abstractmethod
    def find_all(self) -> List[Task]:
        """Busca todas as tarefas"""
        pass

    @abstractmethod
    def update(self, task: Task) -> Task:
        """Atualiza uma tarefa"""
        pass

    @abstractmethod
    def delete_by_id(self, task_id: str) -> bool:
        """Remove uma tarefa por ID"""
        pass

    @abstractmethod
    def count_all(self) -> int:
        """Conta o total de tarefas"""
        pass
