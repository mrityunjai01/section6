from models.user import UserModel
from werkzeug.security import safe_str_cmp
# users = [
# 	User(1 ,'bob', 'asdf')
# ]

# username_mapping = {
# 	u.username: u for u in users
# }

# userid_mapping = {
# 	u.id: u for u in users
# }

def authenticate (uername, password):
	user = UserModel.find_by_username(uername)
	if user and safe_str_cmp(user.password, password):
		return user

def identity(payload):
	return UserModel.find_by_id(payload["identity"])