from flask import request
from flask_restx import Resource, Namespace

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        # all_movies = movie_service.get_all()
        # return movies_schema.dump(all_movies), 200
        return 'ok', 200

    def post(self):
        # data = request.json
        # movie_service.add_new(data)
        return '', 201


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid):
        # movie = movie_service.get_one(mid)
        # return movie_schema.dump(movie), 200
        return '1', 200

    def put(self, mid):
        # data = request.json
        # data['mid'] = mid
        # movie_service.update(data)
        return '', 204

    def patch(self, mid):
        # data = request.json
        # data['mid'] = mid
        # movie_service.update_partial(data)
        return '', 204

    def delete(self, mid):
        # movie_service.delete(mid)
        return '', 204
