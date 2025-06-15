from typing import Optional

from src.domain.database import Database
from ..domain.category import Category
from ..domain.exceptions import TaskNotFoundError

# (pode ser usado com qualquer Database[Category], inclusive DictCategoryDatabase)


class UpdateCategoryUseCase:
    def __init__(self, category_repository: Database[Category]):
        self._category_repository = category_repository

    def execute(
        self,
        category_id: str,
        name: Optional[str] = None,
        description: Optional[str] = None,
    ) -> Category:
        category = self._category_repository.find_by_id(category_id)
        if not category:
            raise TaskNotFoundError(f"Categoria com ID {category_id} não encontrada")
        if name is not None:
            category._validate_name(name)
            category.name = name.strip()
        if description is not None:
            category.description = description.strip() if description else None
        return self._category_repository.update(category)
