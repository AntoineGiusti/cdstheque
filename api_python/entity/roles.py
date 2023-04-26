
class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer,primary_key=True)
    role_name = db.Column(db.String(80),unique=True, nullable=False)