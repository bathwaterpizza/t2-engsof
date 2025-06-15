import pytest
from src.domain.category import Category
from src.domain.task import Task


def test_create_category():
    cat = Category("Trabalho")
    assert cat.name == "Trabalho"
    assert cat.description is None
    assert isinstance(cat.id, str)
    assert cat.tasks == []


def test_create_category_with_description():
    cat = Category("Pessoal", "Coisas do dia a dia")
    assert cat.name == "Pessoal"
    assert cat.description == "Coisas do dia a dia"


def test_category_name_validation():
    with pytest.raises(ValueError):
        Category("")
    with pytest.raises(ValueError):
        Category(" ")
    with pytest.raises(ValueError):
        Category("x" * 101)


def test_add_and_remove_task():
    cat = Category("Estudos")
    task1 = Task("Ler artigo")
    task2 = Task("Fazer exercício")
    cat.add_task(task1)
    cat.add_task(task2)
    assert task1 in cat.tasks
    assert task2 in cat.tasks
    cat.remove_task(task1)
    assert task1 not in cat.tasks
    assert task2 in cat.tasks


def test_to_dict_and_from_dict():
    cat = Category("Viagem", "Planejamento de viagem")
    task = Task("Comprar passagens")
    cat.add_task(task)
    d = cat.to_dict()
    assert d["name"] == "Viagem"
    assert d["description"] == "Planejamento de viagem"
    assert d["tasks"] == [task.id]
    # Test from_dict
    lookup = {task.id: task}
    cat2 = Category.from_dict(d, tasks_lookup=lookup)
    assert cat2.name == cat.name
    assert cat2.description == cat.description
    assert cat2.tasks[0] == task
