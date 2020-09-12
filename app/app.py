import os
from flask import Flask

from sheets import get_weekly_recipes


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        return "is online"

    @app.route("/get-recipe")
    def get_recipe():
       return get_weekly_recipes()

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=os.environ.get("PORT", 5000))
