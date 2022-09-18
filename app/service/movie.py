class MovieService:
    def __init__(self, dao):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_one(self, mid):
        return self.dao.get_by_id(mid)

    def add_new(self, data):
        return self.dao.add_new(data)

    def update(self, mid, **kwargs):
        self.dao.update(mid, **kwargs)

    def get_by_fields(self, **kwargs):
        return self.dao.get_by_fields(**kwargs)

    def delete(self, mid):
        self.dao.delete(mid)
