"""
Ponto de entrada da aplicação To-Do List
"""

from flask import Flask, render_template


def create_app():
    """Factory function para criar a aplicação Flask"""
    app = Flask(__name__)

    # Configurações básicas
    app.config["SECRET_KEY"] = "dev-secret-key"  # Apenas para desenvolvimento

    @app.route("/")
    def index():
        return render_template("index.html")

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
