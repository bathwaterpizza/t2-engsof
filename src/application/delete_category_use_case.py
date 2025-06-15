from src.domain.category import Category
from src.domain.database import Database
from ..domain.exceptions import TaskNotFoundError


# (pode ser usado com qualquer Database[Category], inclusive DictCategoryDatabase)
class DeleteCategoryUseCase:
    def __init__(self, category_repository: Database[Category]):
        self._category_repository = category_repository

    def execute(self, category_id: str) -> bool:
        category = self._category_repository.find_by_id(category_id)
        if not category:
            raise TaskNotFoundError(f"Categoria com ID {category_id} não encontrada")
        return self._category_repository.delete_by_id(category_id)
