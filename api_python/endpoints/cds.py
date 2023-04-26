from flask_restx import Resource, fields, Namespace
from database.database_init import db
from entity.CDS import CDS

ns = Namespace('cds', description='API pour gérer les CDS')

cds_model=ns.model('CDS', {
    'artist':fields.String,
    'album_name':fields.String,
    'year_published':fields.String,
})

@ns.route('/', methods=['GET','POST'])
class CDSList(Resource):
    def get(self):
        return [cd.to_dict() for cd in CDS.query.order_by(CDS.artist).all()]

    # Créer une méthode POST 
    @ns.expect(cds_model)
    def post(self):
        cd = CDS(**ns.payload)        
        db.session.add(cd)
        db.session.commit()                       
        return cd.to_dict()
    
@ns.route('/id/<string:id>', methods=['GET', 'PUT', 'DELETE']) 
class ManageById(Resource):
    # get cd by id
    def get(self, id : str):        
        cd = CDS.query.filter_by(id = id).first()
        return cd.to_dict()

    # Créer une méthode PUT 
    @ns.expect(cds_model)
    def put(self, id : str):
        cd_data = ns.payload
        cd = CDS.query.filter_by(id = id).first()
        if cd is None:
            ns.abort(404, 'CDS not found')
        for key, value in cd_data.items():
            setattr(cd, key, value)
        db.session.commit()
        return cd.to_dict()
 
    # Créer une méthode DELETE
    def delete(self, id : str):        
        cd = CDS.query.filter_by(id = id).first()
        if cd:
            db.session.delete(cd)
            db.session.commit()
            return {'message': f'Le CD {cd.album_name} a été supprimé de la base de données.'}
        ns.abort(404, 'CDS not found')
        
@ns.route('/artist/<string:artist>', methods=['GET']) 
class ManageByartist(Resource):
    # get cd by artist
    def get(self, artist : str):        
        cds = CDS.query.filter(CDS.artist.like(f"{artist}%")).all()
        return [cd.to_dict() for cd in cds]

