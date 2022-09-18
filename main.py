from flask import Flask
from flask_restx import Api

from app.config import Config
from app.db_manager.fill_db import fill_db
from app.setup_db import db
from app.class_based_views.genre import genre_ns
from app.class_based_views.movie import movie_ns
from app.class_based_views.director import director_ns



def create_app(config: Config) -> Flask:
    application = Flask(__name__)
    application.config.from_object(config)
    application.app_context().push()
    return application


def configure_app(application: Flask):
    db.init_app(application)
    api = Api(application)
    api.add_namespace(movie_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(director_ns)


if __name__ == '__main__':
    fill_db()
    app_config = Config()
    app = create_app(app_config)
    configure_app(app)

    app.run()
