from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT
from security import authenticate, identity
from models.user import UserModel
from resources import item, user, store
from os import environ
app = Flask(__name__)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///data.db'
app.config["PROPAGATE_EXCEPTIONS"] = True
app.secret_key = "hj"

api = Api(app)


jwt = JWT(app, authenticate, identity)


api.add_resource(item.Item, '/item/<string:name>')
api.add_resource(item.Items, '/items')
api.add_resource(user.UserRegister, '/register')
api.add_resource(user.User, '/user/<int:user_id>')
api.add_resource(store.Store, '/store/<string:name>')
api.add_resource(store.StoreList, '/stores')
