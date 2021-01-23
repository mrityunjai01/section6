from flask_jwt import jwt_required
from flask_restful import Resource, reqparse
from models.item import ItemModel
class Item (Resource):
	parser = reqparse.RequestParser()
	parser.add_argument('price',
		type=float,
		required = True,
		help = "This field cannot be left empty"
	)
	parser.add_argument('store_id',
		type=int,
		required = True,
		help = "every item needs a store id"
	)
	@jwt_required()
	def get(self, name):
		row = ItemModel.find_by_name(name)
		if row:
			return row.json()
		return {'message': 'item not found'}, 400

	def post (self, name):
		if (ItemModel.find_by_name(name)):
			return {"message": "an item of the same name exists here",
					"item" : ItemModel.find_by_name(name)["item"]}, 400

		data = Item.parser.parse_args()
		item = ItemModel(name, **data)
		try:
			item.save_to_db()
		except:
			return {"message": "trouble inserting item"}
		return item.json(), 201


	def delete(self, name):
		item = ItemModel.find_by_name(name)
		if item:
			item.delete_from_db()
		return {"message": "deleted successfully"}
	def put(self, name):
		# data = request.get_json()
		data = Item.parser.parse_args()
		item = ItemModel.find_by_name(name)

		if item is None:
			item = ItemModel(name, **data)

		else:
			item.price = data["price"]
		item.save_to_db()
		return item.json()

class Items(Resource):
	def get (self):
		return {'items': [item.json() for item in ItemModel.find_all()]}
