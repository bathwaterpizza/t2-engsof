"""
Ponto de entrada da aplicação To-Do List
"""

from flask import Flask, render_template
from src.presentation.task_routes import task_bp
from src.presentation.category_routes import category_bp


def create_app():
    """Factory function para criar a aplicação Flask"""
    app = Flask(__name__)

    # Configurações básicas
    app.config["SECRET_KEY"] = "dev-secret-key"  # Apenas para desenvolvimento

    # Registro dos blueprints das rotas de API
    app.register_blueprint(task_bp)
    app.register_blueprint(category_bp)

    @app.route("/")
    def index():
        return render_template("index.html")

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
