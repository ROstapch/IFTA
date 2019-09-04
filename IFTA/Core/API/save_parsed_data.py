from ..models import *


def save_drivers(drivers_list):
	for driver in drivers_list:
		try:
			driver_info = {
				"driver_name": driver.user_first_name,
				"driver_lastname" : driver.user_last_name,
				"driver_phone" : driver.user_phone,
				"driver_email" : driver.user_email,
				"driver_status" : driver.user_status}
			obj, created = Driver.objects.update_or_create(driver_id = driver.user_id, defaults = driver_info)
			if created:
				print(str(obj) + "  - created")
			else:
				print(str(obj) + "  - edited")
		except Exception:
			pass


def save_units(unit_list):
	for unit in unit_list:
		try:
			comp = Company.objects.get(company_id = unit.unit_company)
			unit_info = {
				"unit_company": comp,
				"unit_eld" : unit.unit_eld,
				"unit_active" : unit.unit_status,
				"unit_ifta" : unit.unit_ifta}
			obj, created = Unit.objects.update_or_create(unit_id = unit.unit_id, unit_number = unit.unit_number, defaults = unit_info)
			if created:
				print(str(obj) + "  - created")
			else:
				print(str(obj) + "  - edited")
		except Exception:
			pass


