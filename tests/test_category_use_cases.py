import pytest
from src.domain.category import Category
from src.application.create_category_use_case import CreateCategoryUseCase
from src.application.get_all_categories_use_case import GetAllCategoriesUseCase
from src.application.update_category_use_case import UpdateCategoryUseCase
from src.application.delete_category_use_case import DeleteCategoryUseCase
from src.infrastructure.dict_category_database import DictCategoryDatabase
from src.domain.exceptions import TaskNotFoundError


def test_create_category_use_case():
    repo = DictCategoryDatabase()
    use_case = CreateCategoryUseCase(repo)
    cat = use_case.execute("Trabalho", "Coisas do trabalho")
    assert cat.name == "Trabalho"
    assert cat.description == "Coisas do trabalho"
    assert repo.count_all() == 1


def test_get_all_categories_use_case():
    repo = DictCategoryDatabase()
    use_case = GetAllCategoriesUseCase(repo)
    assert use_case.execute() == []
    cat1 = Category("A")
    cat2 = Category("B")
    repo.save(cat1)
    repo.save(cat2)
    cats = use_case.execute()
    assert len(cats) == 2
    assert cat1 in cats and cat2 in cats


def test_update_category_use_case():
    repo = DictCategoryDatabase()
    cat = Category("Original", "Desc")
    repo.save(cat)
    use_case = UpdateCategoryUseCase(repo)
    updated = use_case.execute(cat.id, name="Novo", description="Nova desc")
    assert updated.name == "Novo"
    assert updated.description == "Nova desc"
    # Test not found
    with pytest.raises(TaskNotFoundError):
        use_case.execute("id-inexistente", name="X")


def test_delete_category_use_case():
    repo = DictCategoryDatabase()
    cat = Category("Para deletar")
    repo.save(cat)
    use_case = DeleteCategoryUseCase(repo)
    assert use_case.execute(cat.id) is True
    assert repo.count_all() == 0
    # Test not found
    with pytest.raises(TaskNotFoundError):
        use_case.execute("id-inexistente")
