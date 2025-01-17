class DirectorService:
    def __init__(self, dao):
        self.dao = dao

    def get_one(self, did):
        return self.dao.get_by_id(did)

    def get_all(self):
        return self.dao.get_all()
