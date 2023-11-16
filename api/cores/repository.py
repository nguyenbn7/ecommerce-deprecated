from sqlalchemy.orm import Session


class BaseRepository:
    def __init__(self, db: Session, entity: object) -> None:
        self.db = db
        self.entity = entity

    def get_all(self):
        return self.db.query(self.entity).all()
    
    def get_by_id(self, id: int):
        return self.db.query(self.entity).filter(self.entity.id == id).first()
    
    def save(self, entity: object):
        self.db.add(entity)
        self.db.commit()
        return entity
    
    def any(self):
        return self.db.query(self.entity).count() > 0
