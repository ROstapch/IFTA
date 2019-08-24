

class Fuel_Types():
	dsl = 'Diesel'
	gas = 'Gasoline'
	prop = 'Propane'
	eth = 'Ethanol'
	meth = 'Methanol'
	bio = 'Biodiesel'
	fuel_choice = [
		(dsl, 'diesel'),
		(gas, 'gasoline')
	]


class Currency_Types():
	usd = 'USD'
	cad = 'CAD'
	currency_choice = [
		(usd,'USD'),
		(cad,'CAD')
	]


class Volume_Measures():
	gal = 'gal'
	ltr = 'ltr'
	volume_choice = [
		(gal,'gallons'),
		(ltr,'liter')
	]


class Distance_Measures():
	km = 'km'
	mi = 'mi'
	distance_choice = [
		(km,'kilometers'),
		(mi,'miles')
	]


class Vehicle_Types():
	ifta_units = 'ifta'
	all_units = 'all'
	vehicle_choice = [
		(ifta_units,'ifta'),
		(all_units,'all')
	]