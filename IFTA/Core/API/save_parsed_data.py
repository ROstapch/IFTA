from ..models import *


#comp = Company.objects.get(company_name = "Precise Transportation")
#
#unit, created = Unit.objects.update_or_create(unit_id = 777, unit_number = 666, unit_company = comp,
#	defaults = {"unit_eld": "eld", "unit_active" : True, "unit_ifta" : None, "unit_staff" : None, "unit_type" : None})
def save_drivers(drivers_list):
	for driver in drivers_list:
		driver_info = {
			"driver_name": driver.user_first_name,
			"driver_lastname" : driver.user_last_name,
			"driver_phone" : driver.user_phone,
			"driver_status" : driver.user_status}
		obj, created = Driver.objects.update_or_create(driver_id = driver.user_id, defaults = driver_info)
		if created:
			print(str(obj) + "  - created")
		else:
			print(str(obj) + "  - edited")


