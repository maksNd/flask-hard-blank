from flask import request
from flask_restx import Resource, Namespace

from app.container import movie_service
from app.dao.model.movie import MovieSchema

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        fields = request.args
        return movies_schema.dump(
            movie_service.get_by_fields(**fields)
        ), 200

    def post(self):
        movie_service.add_new(request.json)
        return '', 201


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid):
        movie = movie_service.get_one(mid)
        return movie_schema.dump(movie), 200

    def put(self, mid):
        movie_service.update(mid, **request.json)
        return '', 204

    def patch(self, mid):
        movie_service.update(mid, **request.json)
        return '', 204

    def delete(self, mid):
        movie_service.delete(mid)
        return '', 204
