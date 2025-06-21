import sqlite3
import os
from typing import Any, List, Tuple
from contextlib import contextmanager


class SQLiteBase:
    """Classe base para gerenciar conexões SQLite"""
    
    def __init__(self, db_path: str = "todo_app.db"):
        self.db_path = db_path
        self._init_db()
    
    def _init_db(self):
        """Inicializa o banco de dados com as tabelas necessárias"""
        with self._get_connection() as conn:
            # Tabela de categorias
            conn.execute("""
                CREATE TABLE IF NOT EXISTS categories (
                    id TEXT PRIMARY KEY,
                    name TEXT NOT NULL,
                    description TEXT
                )
            """)
            
            # Tabela de tarefas
            conn.execute("""
                CREATE TABLE IF NOT EXISTS tasks (
                    id TEXT PRIMARY KEY,
                    title TEXT NOT NULL,
                    description TEXT,
                    completed BOOLEAN NOT NULL DEFAULT 0,
                    created_at TEXT NOT NULL,
                    updated_at TEXT NOT NULL,
                    category_id TEXT,
                    FOREIGN KEY (category_id) REFERENCES categories (id)
                )
            """)
            
            conn.commit()
    
    @contextmanager
    def _get_connection(self):
        """Context manager para conexões SQLite"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row  # Para acessar colunas por nome
        try:
            yield conn
        finally:
            conn.close()
    
    def _execute_query(self, query: str, params: Tuple = ()) -> List[sqlite3.Row]:
        """Executa uma query SELECT e retorna os resultados"""
        with self._get_connection() as conn:
            cursor = conn.execute(query, params)
            return cursor.fetchall()
    
    def _execute_command(self, command: str, params: Tuple = ()) -> int:
        """Executa um comando (INSERT, UPDATE, DELETE) e retorna linhas afetadas"""
        with self._get_connection() as conn:
            cursor = conn.execute(command, params)
            conn.commit()
            return cursor.rowcount
