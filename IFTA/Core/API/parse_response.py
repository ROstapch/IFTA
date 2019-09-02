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



class ParsedUnit(object):
	def __init__(self, unit_id = None, unit_number = None, unit_company_id = None, unit_eld = None, unit_active = 'deactivated', unit_ifta = True):
		self.unit_id = unit_id
		self.unit_number = unit_number
		self.unit_company = unit_company_id
		self.unit_eld = unit_eld
		self.unit_status = True if unit_active == 'active' else False
		self.unit_ifta = unit_ifta

	def __str__(self):
		return str(self.unit_number)

	def all(self):
		return {"id" : self.unit_id,
		"number" : self.unit_number,
		"company id" : self.unit_company,
		"ELD id" : self.unit_eld,
		"status" : self.unit_status,
		"ifta" : self.unit_ifta}





class ParseJSON(object):
	#users_list = ParseJSON.users(resp.text)
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

	#user_list = ParseJSON.user(resp.text)
	def user(response_text):
		try:
			user_data = json.loads(response_text)
			parsed_user = ParseJSON.parse_user(user_data)
			return ([parsed_user])
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
		try:
			data = json.loads(response_text)
			key_list = list(data.keys())

			units_data = data.get(key_list[key_list.index('vehicles')])

			units_tuple = []
			for unit_data in units_data:
				units_tuple.append(ParseJSON.parse_unit(unit_data))

			return units_tuple
		except Exception:
			return None


	def unit(response_text):
		try:
			unit_data = json.loads(response_text)
			parsed_unit = ParseJSON.parse_unit(unit_data)

			return ([parsed_unit])
		except Exception:
			return None


	def parse_unit(units_data):
		if 'vehicle' in units_data.keys():
			unit_data = units_data.get('vehicle')
			
			unit_id = unit_data.get('id') if 'id' in unit_data.keys() else None
			unit_number = unit_data.get('number') if 'number' in unit_data.keys() else None
			unit_company_id = unit_data.get('company_id') if 'company_id' in unit_data.keys() else None
			if 'eld_device' in unit_data.keys():
				unit_eld = unit_data.get('eld_device').get('identifier') if unit_data.get('eld_device') and 'identifier' in unit_data.get('eld_device') else None
			unit_active = unit_data.get('status') if 'status' in unit_data.keys() else 'deactivated'
			unit_ifta = unit_data.get('ifta') if 'ifta' in unit_data.keys() else True

			parsed_unit = ParsedUnit(unit_id, unit_number, unit_company_id, unit_eld, unit_active, unit_ifta)

			return(parsed_unit)
		else:
			return None
