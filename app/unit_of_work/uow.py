from sqlalchemy.orm import Session


class unit_of_work:

    def __init__(self,db:Session):
        self.db=db
    
    def commit(self):
        self.db.commit()

    def rollback(self):
        self.db.rollback()
        