from typing import Optional

from src.domain.database import Database
from ..domain.category import Category


class CreateCategoryUseCase:
    def __init__(self, category_repository: Database[Category]):
        self._category_repository = category_repository

    def execute(self, name: str, description: Optional[str] = None) -> Category:
        category = Category(name=name, description=description)
        return self._category_repository.save(category)
