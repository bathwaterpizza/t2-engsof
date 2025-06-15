from abc import ABC, abstractmethod
from typing import List, Optional


class Database[T](ABC):
    """Interface para banco de dados genérico"""

    @abstractmethod
    def save(self, entity: T) -> T:
        """Salva uma entidade"""
        pass

    @abstractmethod
    def find_by_id(self, entity_id: str) -> Optional[T]:
        """Busca uma entidade por ID"""
        pass

    @abstractmethod
    def find_all(self) -> List[T]:
        """Busca todas as entidades"""
        pass

    @abstractmethod
    def update(self, entity: T) -> T:
        """Atualiza uma entidade"""
        pass

    @abstractmethod
    def delete_by_id(self, entity_id: str) -> bool:
        """Remove uma entidade por ID"""
        pass

    @abstractmethod
    def count_all(self) -> int:
        """Conta o total de entidades"""
        pass
