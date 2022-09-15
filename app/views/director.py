from flask_restx import Resource, Namespace

director_ns = Namespace('directors')


@director_ns.route('/')
class directorsView(Resource):
    def get(self):
        # directors = director_service.get_all()
        # return directors_schema.dump(directors), 200
        return '1', 200


@director_ns.route('/<int:gid>')
class directorView(Resource):
    def get(self, gid):
        # director = director_service.get_one(gid)
        # return director_schema.dump(director), 200
        return [], 200
