from database.database_init import db

class Status(db.Model):
    __tablename__='status'
    id = db.Column(db.Integer,primary_key=True)
    status_name = db.Column(db.String(80), unique=False, nullable=False)
