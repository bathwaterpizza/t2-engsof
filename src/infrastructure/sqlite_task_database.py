from typing import List, Optional
from datetime import datetime

from ..domain.database import Database
from ..domain.task import Task
from .sqlite_base import SQLiteBase


class SQLiteTaskDatabase(Database[Task], SQLiteBase):
    """Implementação SQLite para o repositório de tarefas"""
    
    def __init__(self, db_path: str = "todo_app.db"):
        SQLiteBase.__init__(self, db_path)
    
    def save(self, task: Task) -> Task:
        """Salva uma tarefa no banco de dados"""
        query = """
            INSERT OR REPLACE INTO tasks 
            (id, title, description, completed, created_at, updated_at, category_id)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        params = (
            task.id,
            task.title,
            task.description,
            task.completed,
            task.created_at.isoformat(),
            task.updated_at.isoformat(),
            task.category_id
        )
        self._execute_command(query, params)
        return task
    
    def find_by_id(self, task_id: str) -> Optional[Task]:
        """Busca uma tarefa por ID"""
        query = "SELECT * FROM tasks WHERE id = ?"
        results = self._execute_query(query, (task_id,))
        
        if not results:
            return None
        
        row = results[0]
        return self._row_to_task(row)
    
    def find_all(self) -> List[Task]:
        """Busca todas as tarefas"""
        query = "SELECT * FROM tasks ORDER BY created_at DESC"
        results = self._execute_query(query)
        
        return [self._row_to_task(row) for row in results]
    
    def update(self, task: Task) -> Task:
        """Atualiza uma tarefa no banco de dados"""
        # Para SQLite, update é o mesmo que save com INSERT OR REPLACE
        return self.save(task)
    
    def delete_by_id(self, task_id: str) -> bool:
        """Remove uma tarefa do banco de dados"""
        query = "DELETE FROM tasks WHERE id = ?"
        rows_affected = self._execute_command(query, (task_id,))
        return rows_affected > 0
    
    def delete(self, task_id: str) -> bool:
        """Remove uma tarefa do banco de dados (método legacy)"""
        return self.delete_by_id(task_id)
    
    def count_all(self) -> int:
        """Retorna o número total de tarefas"""
        query = "SELECT COUNT(*) as count FROM tasks"
        results = self._execute_query(query)
        return results[0]["count"] if results else 0
    
    def find_by_category(self, category_id: str) -> List[Task]:
        """Busca todas as tarefas de uma categoria específica"""
        query = "SELECT * FROM tasks WHERE category_id = ? ORDER BY created_at DESC"
        results = self._execute_query(query, (category_id,))
        
        return [self._row_to_task(row) for row in results]
    
    def count(self) -> int:
        """Retorna o número total de tarefas (método legacy)"""
        return self.count_all()
    
    def _row_to_task(self, row) -> Task:
        """Converte uma linha do banco de dados em uma instância de Task"""
        return Task(
            title=row["title"],
            description=row["description"],
            task_id=row["id"],
            completed=bool(row["completed"]),
            created_at=datetime.fromisoformat(row["created_at"]),
            updated_at=datetime.fromisoformat(row["updated_at"]),
            category_id=row["category_id"]
        )
