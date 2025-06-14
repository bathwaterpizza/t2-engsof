"""
Testes para os casos de uso de tarefas
"""

import pytest
from src.domain.task import Task
from src.application.create_task_use_case import CreateTaskUseCase
from src.application.get_all_tasks_use_case import GetAllTasksUseCase
from src.application.update_task_use_case import UpdateTaskUseCase
from src.application.delete_task_use_case import DeleteTaskUseCase
from src.infrastructure.dict_task_database import DictTaskDatabase
from src.domain.exceptions import TaskNotFoundError


class TestCreateTaskUseCase:
    """Testes para criação de tarefas"""

    def test_create_task_success(self):
        """Teste criação de tarefa com sucesso"""
        repository = DictTaskDatabase()
        use_case = CreateTaskUseCase(repository)

        task = use_case.execute("Nova tarefa", "Descrição da tarefa")

        assert task.title == "Nova tarefa"
        assert task.description == "Descrição da tarefa"
        assert not task.completed
        assert repository.count_all() == 1


class TestGetAllTasksUseCase:
    """Testes para listagem de tarefas"""

    def test_get_all_tasks_empty(self):
        """Teste busca em repositório vazio"""
        repository = DictTaskDatabase()
        use_case = GetAllTasksUseCase(repository)

        tasks = use_case.execute()

        assert len(tasks) == 0

    def test_get_all_tasks_with_data(self):
        """Teste busca com tarefas existentes"""
        repository = DictTaskDatabase()
        task1 = Task("Tarefa 1")
        task2 = Task("Tarefa 2")
        repository.save(task1)
        repository.save(task2)

        use_case = GetAllTasksUseCase(repository)
        tasks = use_case.execute()

        assert len(tasks) == 2
        assert task1 in tasks
        assert task2 in tasks


class TestUpdateTaskUseCase:
    """Testes para atualização de tarefas"""

    def test_update_task_title(self):
        """Teste atualização do título da tarefa"""
        repository = DictTaskDatabase()
        task = Task("Título original")
        repository.save(task)

        use_case = UpdateTaskUseCase(repository)
        updated_task = use_case.execute(task.id, title="Novo título")

        assert updated_task.title == "Novo título"

    def test_update_task_description(self):
        """Teste atualização da descrição da tarefa"""
        repository = DictTaskDatabase()
        task = Task("Tarefa", "Descrição original")
        repository.save(task)

        use_case = UpdateTaskUseCase(repository)
        updated_task = use_case.execute(task.id, description="Nova descrição")

        assert updated_task.description == "Nova descrição"

    def test_update_task_completed_status(self):
        """Teste atualização do status de conclusão"""
        repository = DictTaskDatabase()
        task = Task("Tarefa pendente")
        repository.save(task)

        use_case = UpdateTaskUseCase(repository)
        updated_task = use_case.execute(task.id, completed=True)

        assert updated_task.completed is True

    def test_toggle_task_to_pending(self):
        """Teste marcar tarefa como pendente"""
        repository = DictTaskDatabase()
        task = Task("Tarefa concluída", completed=True)
        repository.save(task)

        use_case = UpdateTaskUseCase(repository)
        updated_task = use_case.execute(task.id, completed=False)

        assert updated_task.completed is False

    def test_update_task_not_found(self):
        """Teste atualização de tarefa inexistente"""
        repository = DictTaskDatabase()
        use_case = UpdateTaskUseCase(repository)

        with pytest.raises(TaskNotFoundError):
            use_case.execute("id-inexistente", title="Novo título")


class TestDeleteTaskUseCase:
    """Testes para remoção de tarefas"""

    def test_delete_task_success(self):
        """Teste remoção de tarefa com sucesso"""
        repository = DictTaskDatabase()
        task = Task("Tarefa para deletar")
        repository.save(task)

        use_case = DeleteTaskUseCase(repository)
        result = use_case.execute(task.id)

        assert result is True
        assert repository.count_all() == 0

    def test_delete_task_not_found(self):
        """Teste remoção de tarefa inexistente"""
        repository = DictTaskDatabase()
        use_case = DeleteTaskUseCase(repository)

        with pytest.raises(TaskNotFoundError):
            use_case.execute("id-inexistente")
