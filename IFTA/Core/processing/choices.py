
class Driver_Statuses():
	active = 'active'
	disabled = 'deactivated'
	driver_status_choice = [
		(active, 'active'),
		(disabled, 'deactivated')
	]

class Unit_Groups():
	comp = 'company'
	owner = "owner"
	rent = 'rent'
	lease = 'lease'
	unit_group_choice = [
		(comp, 'Company vehicle'),
		(owner, "Owner's vehicle"),
		(rent, 'Rented vehicle'),
		(lease, 'Leased vehice')
	]
