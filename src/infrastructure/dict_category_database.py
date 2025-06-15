from typing import List, Optional, Dict
from ..domain.category import Category
from ..domain.database import Database


class DictCategoryDatabase(Database[Category]):
    def __init__(self):
        self._categories: Dict[str, Category] = {}

    def save(self, category: Category) -> Category:
        self._categories[category.id] = category
        return category

    def find_by_id(self, category_id: str) -> Optional[Category]:
        return self._categories.get(category_id)

    def find_all(self) -> List[Category]:
        return list(self._categories.values())

    def update(self, category: Category) -> Category:
        if category.id in self._categories:
            self._categories[category.id] = category
        return category

    def delete_by_id(self, category_id: str) -> bool:
        if category_id in self._categories:
            del self._categories[category_id]
            return True
        return False

    def count_all(self) -> int:
        return len(self._categories)
