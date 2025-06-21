#!/usr/bin/env python3

from flask import Flask, request, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db, Newsletter

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///newsletters.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

class Home(Resource):
    def get(self):
        response_dict = {
            'message': 'welcome to the newsletter API'
        }
        response = make_response(
            response_dict,200
        )
        return response

class Newsletters(Resource):
    def get(self):
        response_dict  = [n.to_dict() for n in Newsletter.query.all()]
        response =make_response(
            response_dict, 200
        )
        return response

class NewsletterByID(Resource):
       def get(self,id):
            response_dict = Newsletter.query.filter_by(id =id).first().to_dict()
            response =make_response(response_dict,200)
            return response

api.add_resource(Home,'/')
api.add_resource(Newsletters, '/newsletters')
api.add_resource(NewsletterByID,'/newsletters/<int:id>')


if __name__ == '__main__':
    app.run(port=5555, debug=True)
