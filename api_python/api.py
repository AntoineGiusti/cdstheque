from flask import Flask
from database.database_init import db
from flask_cors import CORS
from flask_restx import Api
from endpoints.cds import ns

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-type'
app.config['CORS_RESOURCES'] = {r"cds/": {"origins": "*"}}
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/mydb.db'

db.init_app(app)

api = Api(app)
api.add_namespace(ns)
 
if __name__ == '__main__': 
    app.run(debug=True)