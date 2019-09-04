from ..models import *
from .api_requests import Company_Drivers, Company_Units
from .parse_response import ParseJSON
from .save_parsed_data import save_drivers, save_units
from .company_key import companies as company_names

class UpdateData(object):

	def update_all():
		UpdateData.companies()
		companies = Company.objects.order_by('company_name')
		for company in companies:
			UpdateData.units_company(comp_name = company.company_name)
			UpdateData.drivers_company(comp_name = company.company_name)


	def companies():
		companies = company_names()

		for company in companies:
			if company:
				new_comp = Company(company_id = None, company_name = company, company_address = "")
				req = Company_Units.Get_All_Units(units_per_page = 1, comp = [new_comp])
				
				resp = req.send_request()
				if resp:
					if resp.status_code == 200:
						unit_list = ParseJSON.units(resp.text)
						new_comp.company_id = unit_list[0].unit_company

					try:
						company_info = {
							"company_id": new_comp.company_id,
						}
						obj, created = Company.objects.update_or_create(company_name = new_comp.company_name, defaults = company_info)

						if created:
							print(str(obj) + "  - created")
						else:
							print(str(obj) + "  - edited")
					except Exception:
						pass

					else:
						print(resp.status_code)
				else:
					print("Errors with request using given company api key")
			else:
				print("No company with such name")




	def drivers_company(per_page = 50, comp_name = None):
		if Company.objects.all():
			company = Company.objects.filter(company_name=comp_name)
			if company:
				req = Company_Drivers.Get_All_Drivers(users_per_page = per_page, comp = company)

				while (req.page_no.get('page_no') <= req.total_pages):
					resp = req.send_request()
					req.page_no['page_no'] += 1
					if resp:
						if resp.status_code == 200:
							req.total_pages = ParseJSON.total_pages(resp.text)
							user_list = ParseJSON.users(resp.text)
							save_drivers(user_list)
						else:
							print(resp.status_code)
					else:
						print("Errors with request")


			else:
				print("No company with such name")
		else:
			print("No companies available")




	def units_company(per_page = 50, comp_name = None):
		if Company.objects.all():
			company = Company.objects.filter(company_name=comp_name)
			if company:
				req = Company_Units.Get_All_Units(units_per_page = per_page, comp = company)

				while (req.page_no.get('page_no') <= req.total_pages):
					resp = req.send_request()
					req.page_no['page_no'] += 1
					if resp:
						if resp.status_code == 200:
							req.total_pages = ParseJSON.total_pages(resp.text)
							unit_list = ParseJSON.units(resp.text)
							save_units(unit_list)
						else:
							print(resp.status_code)
					else:
						print("Errors with request")


			else:
				print("No company with such name")
		else:
			print("No companies available")