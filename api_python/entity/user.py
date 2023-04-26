from database.database_init import db

class User(db.Model): 
    __tablename__='user'
    id = db.Column(db.Integer,primary_key=True)
    lastname = db.Column(db.String(80), unique=False, nullable=False)
    firstname = db.Column(db.String(80), unique=True, nullable=False)
    role = db.Column(db.String(80), unique=True, nullable=False)
     