from app.dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Movie).all()

    def get_by_id(self, mid):
        return self.session.query(Movie).get(mid)

    def get_by_fields(self, **kwargs):
        return self.session.query(Movie).filter_by(**kwargs).all()

    def add_new(self, data):
        movie = Movie(**data)
        self.session.add(movie)
        self.session.commit()

    def update(self, mid, **kwargs):
        self.session.query(Movie).filter(Movie.id == mid).update(
            kwargs
        )
        self.session.commit()

    def delete(self, mid):
        movie = self.get_by_id(mid)
        self.session.delete(movie)
        self.session.commit()
