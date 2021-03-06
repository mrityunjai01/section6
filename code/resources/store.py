from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):
	def get(self, name):
		store = StoreModel.find_by_name(name)
		if store:
			return store.json()
		return {"message": "store not found"}, 404
		
	def post(self, name):
		if (StoreModel.find_by_name(name)):
			return {"message": "a store with the same name exists"}
		store = StoreModel(name)
		try:
			store.save_to_db()
		except:
			return {"message": "error occurred"}, 500
		return {"message": "created the store"}

	def delete(self, name):
		store = StoreModel.find_by_name(name)
		if (store):
			store.delete_from_db()
			return {"message": "successful deletion"}
		return {"message": "cant find, so cant delete"}


class StoreList(Resource):
	def get(self):
		return {'stores': [store.json() for store in StoreModel.query.all()]}