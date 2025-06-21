from flask import Blueprint, request, jsonify
from src.infrastructure.sqlite_task_database import SQLiteTaskDatabase
from src.application.create_task_use_case import CreateTaskUseCase
from src.application.get_all_tasks_use_case import GetAllTasksUseCase
from src.application.update_task_use_case import UpdateTaskUseCase
from src.application.delete_task_use_case import DeleteTaskUseCase
from src.domain.exceptions import TaskNotFoundError


task_bp = Blueprint("task_bp", __name__, url_prefix="/api/tasks")
task_repo = SQLiteTaskDatabase()


@task_bp.route("/", methods=["POST"])
def create_task():
    data = request.get_json()
    title = data.get("title")
    description = data.get("description")
    category_id = data.get("category_id")  # Novo: lê o campo category_id
    use_case = CreateTaskUseCase(task_repo)
    try:
        task = use_case.execute(
            title, description, category_id=category_id
        )  # Passa category_id
        return jsonify(task.to_dict()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@task_bp.route("/", methods=["GET"])
def get_all_tasks():
    use_case = GetAllTasksUseCase(task_repo)
    tasks = use_case.execute()
    return jsonify([t.to_dict() for t in tasks]), 200


@task_bp.route("/<task_id>", methods=["PUT", "PATCH"])
def update_task(task_id):
    data = request.get_json()
    title = data.get("title")
    description = data.get("description")
    completed = data.get("completed")
    category_id = data.get("category_id")  # Novo: lê o campo category_id
    use_case = UpdateTaskUseCase(task_repo)
    try:
        task = use_case.execute(
            task_id,
            title=title,
            description=description,
            completed=completed,
            category_id=category_id,  # Passa category_id
        )
        return jsonify(task.to_dict()), 200
    except TaskNotFoundError as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@task_bp.route("/<task_id>", methods=["DELETE"])
def delete_task(task_id):
    use_case = DeleteTaskUseCase(task_repo)
    try:
        use_case.execute(task_id)
        return "", 204
    except TaskNotFoundError as e:
        return jsonify({"error": str(e)}), 404
