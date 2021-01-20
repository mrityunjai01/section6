from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT
from security import authenticate, identity
from models.user import UserModel
from resources import item, user, store
app = Flask(__name__)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///data.db'

app.secret_key = "hj"

api = Api(app)


jwt = JWT(app, authenticate, identity)


api.add_resource(item.Item, '/item/<string:name>')
api.add_resource(item.Items, '/items')
api.add_resource(user.UserRegister, '/register')
api.add_resource(store.Store, '/store/<string:name>')
api.add_resource(store.StoreList, '/stores')
if __name__ == '__main__':
	from os import environ
	app.run (host= '0.0.0.0', port = environ.get("PORT", 5050), debug = True)
