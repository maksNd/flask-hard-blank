class MovieService:
    def __init__(self, dao):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_one(self, mid):
        return self.dao.get_by_id(mid)

    def add_new(self, data):
        return self.dao.add_new(data)

    def update(self, data):
        mid = data.get('id')
        movie = self.get_one(mid)
        movie.id = data.get('id')
        movie.title = data.get('title')
        movie.description = data.get('description')
        movie.trailer = data.get('trailer')
        movie.year = data.get('year')
        movie.rating = data.get('rating')
        movie.genre_id = data.get('genre_id')
        movie.director_id = data.get('director_id')
        self.dao.update(movie)

    def get_by_field(self, genre):
        ...

    def delete(self, mid):
        self.dao.delete(mid)
