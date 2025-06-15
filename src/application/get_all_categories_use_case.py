from typing import List

from src.domain.database import Database
from ..domain.category import Category


# (pode ser usado com qualquer Database[Category], inclusive DictCategoryDatabase)
class GetAllCategoriesUseCase:
    def __init__(self, category_repository: Database[Category]):
        self._category_repository = category_repository

    def execute(self) -> List[Category]:
        return self._category_repository.find_all()
