"""
Testes básicos para a entidade Task
"""

import pytest
from datetime import datetime
from src.domain.task import Task


def test_create_task_with_title():
    """Teste criação de tarefa com título apenas"""
    task = Task("Minha primeira tarefa")

    assert task.title == "Minha primeira tarefa"
    assert task.description is None
    assert task.completed is False
    assert task.id is not None
    assert isinstance(task.created_at, datetime)
    assert isinstance(task.updated_at, datetime)


def test_create_task_with_description():
    """Teste criação de tarefa com descrição"""
    task = Task("Tarefa com descrição", "Esta é uma descrição detalhada")

    assert task.title == "Tarefa com descrição"
    assert task.description == "Esta é uma descrição detalhada"


def test_task_validation_empty_title():
    """Teste validação de título vazio"""
    with pytest.raises(ValueError, match="Título da tarefa não pode ser vazio"):
        Task("")


def test_task_validation_long_title():
    """Teste validação de título muito longo"""
    long_title = "x" * 201
    with pytest.raises(
        ValueError, match="Título da tarefa deve ter no máximo 200 caracteres"
    ):
        Task(long_title)


def test_mark_task_as_completed():
    """Teste marcar tarefa como concluída"""
    task = Task("Tarefa para completar")
    old_updated_at = task.updated_at

    task.mark_as_completed()

    assert task.completed is True
    assert task.updated_at > old_updated_at


def test_mark_task_as_pending():
    """Teste marcar tarefa como pendente"""
    task = Task("Tarefa concluída", completed=True)
    old_updated_at = task.updated_at

    task.mark_as_pending()

    assert task.completed is False
    assert task.updated_at > old_updated_at


def test_update_task_title():
    """Teste atualização do título"""
    task = Task("Título original")
    old_updated_at = task.updated_at

    task.update_title("Novo título")

    assert task.title == "Novo título"
    assert task.updated_at > old_updated_at


def test_task_to_dict():
    """Teste conversão para dicionário"""
    task = Task("Tarefa teste", "Descrição teste")
    task_dict = task.to_dict()

    assert task_dict["title"] == "Tarefa teste"
    assert task_dict["description"] == "Descrição teste"
    assert task_dict["completed"] is False
    assert "id" in task_dict
    assert "created_at" in task_dict
    assert "updated_at" in task_dict


def test_task_from_dict():
    """Teste criação a partir de dicionário"""
    data = {
        "id": "test-id-123",
        "title": "Tarefa do dict",
        "description": "Descrição do dict",
        "completed": True,
        "created_at": "2023-01-01T12:00:00",
        "updated_at": "2023-01-01T12:00:00",
    }

    task = Task.from_dict(data)

    assert task.id == "test-id-123"
    assert task.title == "Tarefa do dict"
    assert task.description == "Descrição do dict"
    assert task.completed is True


def test_task_equality():
    """Teste comparação de igualdade entre tarefas"""
    task1 = Task("Tarefa 1", task_id="same-id")
    task2 = Task("Tarefa 2", task_id="same-id")
    task3 = Task("Tarefa 3", task_id="different-id")

    assert task1 == task2  # Mesmo ID
    assert task1 != task3  # IDs diferentes


def test_create_task_with_category():
    """Teste criação de tarefa com categoria"""
    task = Task("Tarefa com categoria", category_id="cat-123")
    assert task.category_id == "cat-123"


def test_task_to_dict_with_category():
    """Teste conversão para dicionário incluindo categoria"""
    task = Task("Tarefa com categoria", category_id="cat-xyz")
    d = task.to_dict()
    assert d["category_id"] == "cat-xyz"


def test_task_from_dict_with_category():
    """Teste criação a partir de dicionário com categoria"""
    data = {
        "id": "id-1",
        "title": "Tarefa",
        "category_id": "cat-abc",
        "created_at": "2025-06-14T00:00:00",
        "updated_at": "2025-06-14T00:00:00",
    }
    task = Task.from_dict(data)
    assert task.category_id == "cat-abc"
