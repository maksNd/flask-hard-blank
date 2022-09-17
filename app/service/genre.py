class GenreService:
    def __init__(self, dao):
        self.dao = dao

    def get_one(self, gid):
        return self.dao.get_by_id(gid)

    def get_all(self):
        return self.dao.get_all()
