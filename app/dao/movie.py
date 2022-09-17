from app.dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Movie).all()

    def get_by_id(self, mid):
        return self.session.query(Movie).get(mid)

    def get_by_director(self, director_id):
        return self.session.query(Movie).filter(Movie.director_id == director_id).all()

    def get_by_genre(self, genre_id):
        return self.session.query(Movie).filter(Movie.genre_id == genre_id).all()

    def get_by_year(self, year):
        return self.session.query(Movie).filter(Movie.year == year).all()

    def add_new(self, data):
        movie = Movie(**data)
        self.session.add(movie)
        self.session.commit()

    def update(self, movie):
        self.session.add(movie)
        self.session.commit()

    def delete(self, mid):
        movie = self.get_by_id(mid)
        self.session.add(movie)
        self.session.commit()
