from flask_restx import Resource, Namespace

from app.container import director_service
from app.dao.model.director import DirectorSchema

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        directors = director_service.get_all()
        return directors_schema.dump(directors), 200


@director_ns.route('/<int:gid>')
class DirectorView(Resource):
    def get(self, gid):
        director = director_service.get_one(gid)
        return director_schema.dump(director), 200
