from typing import List, Optional

from ..domain.database import Database
from ..domain.category import Category
from .sqlite_base import SQLiteBase


class SQLiteCategoryDatabase(Database[Category], SQLiteBase):
    """Implementação SQLite para o repositório de categorias"""
    
    def __init__(self, db_path: str = "todo_app.db"):
        SQLiteBase.__init__(self, db_path)
    
    def save(self, category: Category) -> Category:
        """Salva uma categoria no banco de dados"""
        query = """
            INSERT OR REPLACE INTO categories 
            (id, name, description)
            VALUES (?, ?, ?)
        """
        params = (
            category.id,
            category.name,
            category.description
        )
        self._execute_command(query, params)
        return category
    
    def find_by_id(self, category_id: str) -> Optional[Category]:
        """Busca uma categoria por ID"""
        query = "SELECT * FROM categories WHERE id = ?"
        results = self._execute_query(query, (category_id,))
        
        if not results:
            return None
        
        row = results[0]
        return self._row_to_category(row)
    
    def find_all(self) -> List[Category]:
        """Busca todas as categorias"""
        query = "SELECT * FROM categories ORDER BY name"
        results = self._execute_query(query)
        
        return [self._row_to_category(row) for row in results]
    
    def update(self, category: Category) -> Category:
        """Atualiza uma categoria no banco de dados"""
        # Para SQLite, update é o mesmo que save com INSERT OR REPLACE
        return self.save(category)
    
    def delete_by_id(self, category_id: str) -> bool:
        """Remove uma categoria do banco de dados"""
        # Primeiro, verifica se há tarefas associadas
        task_query = "SELECT COUNT(*) as count FROM tasks WHERE category_id = ?"
        task_results = self._execute_query(task_query, (category_id,))
        
        if task_results and task_results[0]["count"] > 0:
            # Se há tarefas associadas, primeiro remove a associação
            update_query = "UPDATE tasks SET category_id = NULL WHERE category_id = ?"
            self._execute_command(update_query, (category_id,))
        
        # Remove a categoria
        delete_query = "DELETE FROM categories WHERE id = ?"
        rows_affected = self._execute_command(delete_query, (category_id,))
        return rows_affected > 0
    
    def delete(self, category_id: str) -> bool:
        """Remove uma categoria do banco de dados (método legacy)"""
        return self.delete_by_id(category_id)
    
    def count_all(self) -> int:
        """Retorna o número total de categorias"""
        query = "SELECT COUNT(*) as count FROM categories"
        results = self._execute_query(query)
        return results[0]["count"] if results else 0
    
    def find_by_name(self, name: str) -> Optional[Category]:
        """Busca uma categoria por nome"""
        query = "SELECT * FROM categories WHERE name = ?"
        results = self._execute_query(query, (name,))
        
        if not results:
            return None
        
        row = results[0]
        return self._row_to_category(row)
    
    def count(self) -> int:
        """Retorna o número total de categorias (método legacy)"""
        return self.count_all()
    
    def _row_to_category(self, row) -> Category:
        """Converte uma linha do banco de dados em uma instância de Category"""
        return Category(
            name=row["name"],
            description=row["description"],
            category_id=row["id"]
        )
