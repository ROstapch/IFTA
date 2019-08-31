import json

class ParsedUser(object):
	def __init__(self, user_id = None, first_name = 'Name', last_name = 'Last name', phone = None, status = 'active'):
		self.user_id = user_id
		self.user_first_name = first_name
		self.user_last_name = last_name
		self.user_phone = phone
		self.user_status = status

	def __str__(self):
		return self.user_first_name + " " + self.user_last_name

	def all(self):
		return {"id" : self.user_id,
		"first name" : self.user_first_name,
		"last name" : self.user_last_name,
		"phone" : self.user_phone,
		"status" : self.user_status}


class ParseJSON(object):

	def users(response_text):
		try:
			data = json.loads(response_text)
			key_list = list(data.keys())

			users_data = data.get(key_list[key_list.index('users')])

			users_tuple = []
			for user_data in users_data:
				users_tuple.append(ParseJSON.parse_user(user_data))

			return users_tuple
		except Exception:
			return None


	def user(response_text):
		try:
			user_data = json.loads(response_text)
			parsed_user = ParseJSON.parse_user(user_data)
			return (parsed_user)
		except Exception:
			return None




	def parse_user(user_data):
		if 'user' in user_data.keys():
			user_data = user_data.get('user')
			
			user_id = user_data.get('id') if 'id' in user_data.keys() else None
			user_first_name = user_data.get('first_name') if 'first_name' in user_data.keys() else 'Name'
			user_last_name = user_data.get('last_name') if 'last_name' in user_data.keys() else 'Last name'
			user_phone = user_data.get('phone') if 'phone' in user_data.keys() else None
			user_is_active = user_data.get('status') if 'status' in user_data.keys() else 'active'

			parsed_user = ParsedUser(user_id, user_first_name, user_last_name, user_phone, user_is_active)

			return(parsed_user)
		else:
			return None






	def units(response_text):
		pass


	def unit(response_text):
		pass
