# Rotas RESTful para categorias (Presentation Layer)
# Fornece endpoints para CRUD de categorias usando SQLite
from flask import Blueprint, request, jsonify
from src.infrastructure.sqlite_category_database import SQLiteCategoryDatabase
from src.application.create_category_use_case import CreateCategoryUseCase
from src.application.get_all_categories_use_case import GetAllCategoriesUseCase
from src.application.update_category_use_case import UpdateCategoryUseCase
from src.application.delete_category_use_case import DeleteCategoryUseCase
from src.domain.exceptions import TaskNotFoundError


# Blueprint de categorias
category_bp = Blueprint("category_bp", __name__, url_prefix="/api/categories")
category_repo = SQLiteCategoryDatabase()


@category_bp.route("/", methods=["POST"])
def create_category():
    """Cria uma nova categoria"""
    data = request.get_json()
    name = data.get("name")
    description = data.get("description")
    use_case = CreateCategoryUseCase(category_repo)
    try:
        category = use_case.execute(name, description)
        return jsonify(category.to_dict()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@category_bp.route("/", methods=["GET"])
def get_all_categories():
    """Lista todas as categorias"""
    use_case = GetAllCategoriesUseCase(category_repo)
    categories = use_case.execute()
    return jsonify([c.to_dict() for c in categories]), 200


@category_bp.route("/<category_id>", methods=["PUT", "PATCH"])
def update_category(category_id):
    """Atualiza uma categoria existente"""
    data = request.get_json()
    name = data.get("name")
    description = data.get("description")
    use_case = UpdateCategoryUseCase(category_repo)
    try:
        category = use_case.execute(category_id, name=name, description=description)
        return jsonify(category.to_dict()), 200
    except TaskNotFoundError as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@category_bp.route("/<category_id>", methods=["DELETE"])
def delete_category(category_id):
    """Remove uma categoria pelo ID"""
    use_case = DeleteCategoryUseCase(category_repo)
    try:
        use_case.execute(category_id)
        return "", 204
    except TaskNotFoundError as e:
        return jsonify({"error": str(e)}), 404
