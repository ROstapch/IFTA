import requests
from ..models import *
from .company_key import key_by_name

class Company_Drivers():
	#temp = Company_Drivers.Get_All_Drivers(comp = Company.objects.select_related().filter(company_name="Name"))
	#resp = temp.send_request()
	class Get_All_Drivers(object):
		url = None
		role = None
		duty_status = None
		status = None
		per_page = None
		page_no = None
		metric = None
		total_pages = None
		comp_name = None
		def __init__(self, driver_status = None, users_per_page = 50, page = 1, comp = None):
			# URL of the request
			self.url = "https://api.keeptruckin.com/v1/users"
			# parameters of the request
			self.role = {"role" : "driver"}
			self.duty_status = {"duty_status" : None}
			self.status = {"status" : driver_status}
			self.per_page = {"per_page" : users_per_page}
			self.page_no = {"page_no" : page}
			# headers of the request
			self.metric = {"X-Metric-Units" : None}

			#used to indicate total pages
			self.total_pages = 1
			#used to import correct api key
			if comp:
				self.comp_name = comp[0].company_name
			else:
				self.comp_name = comp


		def send_request(self):
			response = None

			if self.comp_name:

				key_header = key_by_name(self.comp_name)
				if all(key_header.values()):

					request_params = {**self.role, **self.duty_status, **self.status, **self.per_page, **self.page_no}
					request_header = {**key_header, **self.metric}
					response = requests.request(method = 'GET', url=self.url, params = request_params, headers = request_header, timeout = 10)

				key_header = None
			return response



	#temp = Company_Drivers.Get_Driver_Id(drivers_id = 512930, comp = Company.objects.select_related().filter(company_name="Name"))
	#resp = temp.send_request()
	class Get_Driver_Id(object):
		url = None
		driver_id = None
		metric = None
		comp_name = None
		def __init__(self, drivers_id = None, comp = None):
			# URL of the request
			self.url = "https://api.keeptruckin.com/v1/users/%s" % str(drivers_id)
			# parameters of the request
			self.driver_id = {"id" : drivers_id}
			# headers of the request
			self.metric = {"X-Metric-Units" : None}

			#used to import correct api key
			if comp:
				self.comp_name = comp[0].company_name
			else:
				self.comp_name = comp


		def send_request(self):
			response = None

			if self.comp_name:

				key_header = key_by_name(self.comp_name)
				if all(key_header.values()):

					request_params = self.driver_id
					request_header = {**key_header, **self.metric}
					response = requests.request(method = 'GET', url=self.url, params = request_params, headers = request_header, timeout = 10)

				key_header = None
			return response





class Company_Units():
	#temp = Company_Units.Get_All_Units(comp = Company.objects.select_related().filter(company_name="Name"))
	#resp = temp.send_request()
	class Get_All_Units(object):
		url = None
		driver_id = None
		fuel_type= None
		per_page = None
		page_no = None
		metric = None
		total_pages = None
		comp_name = None
		def __init__(self, units_per_page = 50, page = 1, comp = None):
			# URL of the request
			self.url = "https://api.keeptruckin.com/v1/vehicles"
			# parameters of the request
			self.driver_id = {"driver_ids" : None}
			self.fuel_type = {"fuel_type" : None}
			self.per_page = {"per_page" : units_per_page}
			self.page_no = {"page_no" : page}
			# headers of the request
			self.metric = {"X-Metric-Units" : None}

			#used to indicate total pages
			self.total_pages = 1
			#used to import correct api key
			if comp:
				self.comp_name = comp[0].company_name
			else:
				self.comp_name = comp


		def send_request(self):
			response = None

			if self.comp_name:

				key_header = key_by_name(self.comp_name)
				if all(key_header.values()):

					request_params = {**self.driver_id, **self.fuel_type, **self.per_page, **self.page_no}
					request_header = {**key_header, **self.metric}
					response = requests.request(method = 'GET', url=self.url, params = request_params, headers = request_header, timeout = 10)
					
				key_header = None
			return response



	#temp = Company_Units.Get_Unit_Id(units_id = 64801, comp = Company.objects.select_related().filter(company_name="Name"))
	#resp = temp.send_request()
	class Get_Unit_Id(object):
		url = None
		unit_id = None
		metric = None
		comp_name = None
		def __init__(self, units_id = None, comp = None):
			# URL of the request
			self.url = "https://api.keeptruckin.com/v1/vehicles/%s" % str(units_id)
			# parameters of the request
			self.unit_id = {"id" : units_id}
			# headers of the request
			self.metric = {"X-Metric-Units" : None}

			#used to import correct api key
			if comp:
				self.comp_name = comp[0].company_name
			else:
				self.comp_name = comp


		def send_request(self):
			response = None

			if self.comp_name:

				key_header = key_by_name(self.comp_name)
				if all(key_header.values()):

					request_params = self.unit_id
					request_header = {**key_header, **self.metric}
					response = requests.request(method = 'GET', url=self.url, params = request_params, headers = request_header, timeout = 10)

				key_header = None
			return response





class Companies():
	pass
