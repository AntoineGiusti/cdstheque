from database.database_init import db

class CDS(db.Model): 
    __tablename__='cds'
    id = db.Column(db.Integer,primary_key=True)
    artist = db.Column(db.String(80), unique=False, nullable=False)
    album_name = db.Column(db.String(80), unique=True, nullable=False)
    year_published = db.Column(db.String(80), unique=False, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'artist': self.artist,
            'album_name': self.album_name,
            'year_published': self.year_published
        }
