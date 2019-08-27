

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
		(ltr,'liters')
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

class Jurisdiction_list():
	#Canada
	alberta	= "AB"
	british_columbia = "BC"
	manitoba = "MB"
	new_brunswick = "NB"
	newfoundland_labrador = "NL"
	northwest_territories = "NT"
	nova_scotia = "NS"
	nunavut = "NU"
	ontario = "ON"
	prince_edward_island = "PE"
	quebec = "QC"
	saskatchewan = "SK"
	yukon = "YT"
	#USA
	alabama = "AL"
	alaska = "AK"
	arizona = "AZ"
	arkansas = "AR"
	california = "CA"
	colorado = "CO"
	connecticut = "CT"
	delaware = "DE"
	district_columbia = "DC"
	florida = "FL"
	georgia = "GA"
	hawaii = "HI"
	idaho = "ID"
	illinois = "IL"
	indiana = "IN"
	iowa = "IA"
	kansas = "KS"
	kentucky = "KY"
	louisiana  = "LA"
	maine  = "ME"
	maryland  = "MD"
	massachusetts  = "MA"
	michigan = "MI"
	minnesota = "MN"
	mississippi = "MS"
	missouri = "MO"
	montana = "MT"
	nebraska  = "NE"
	nevada = "NV"
	new_hampshire  = "NH"
	new_jersey  = "NJ"
	new_mexico = "NM"
	new_york  = "NY"
	north_carolina = "NC"
	north_dakota = "ND"
	ohio = "OH"
	oklahoma = "OK"
	oregon= "OR"
	pennsylvania = "PA"
	rhode_island = "RI"
	south_carolina = "SC"
	south_dakota = "SD"
	tennessee = "TN"
	texas = "TX"
	utah = "UT"
	vermont = "VT"
	virginia = "VA"
	washington = "WA"
	west_virginia = "WV"
	wisconsin = "WI"
	wyoming = "WY"

	jurisdiction_choice = [
		#USA
		(alabama , "AL"),
		(alaska , "AK"),
		(arizona , "AZ"),
		(arkansas , "AR"),
		(california , "CA"),
		(colorado , "CO"),
		(connecticut , "CT"),
		(delaware , "DE"),
		(district_columbia , "DC"),
		(florida , "FL"),
		(georgia , "GA"),
		(idaho , "ID"),
		(illinois , "IL"),
		(indiana , "IN"),
		(iowa , "IA"),
		(kansas , "KS"),
		(kentucky , "KY"),
		(louisiana  , "LA"),
		(maine  , "ME"),
		(maryland  , "MD"),
		(massachusetts  , "MA"),
		(michigan , "MI"),
		(minnesota , "MN"),
		(mississippi , "MS"),
		(missouri , "MO"),
		(montana , "MT"),
		(nebraska  , "NE"),
		(nevada , "NV"),
		(new_hampshire  , "NH"),
		(new_jersey  , "NJ"),
		(new_mexico , "NM"),
		(new_york  , "NY"),
		(north_carolina , "NC"),
		(north_dakota , "ND"),
		(ohio , " OH"),
		(oklahoma , " OK"),
		(oregon , " OR"),
		(pennsylvania , " PA"),
		(rhode_island , "RI"),
		(south_carolina , "SC"),
		(south_dakota , "SD"),
		(tennessee , "TN"),
		(texas , "TX"),
		(utah , "UT"),
		(vermont , "VT"),
		(virginia , "VA"),
		(washington , "WA"),
		(west_virginia , "WV"),
		(wisconsin , "WI"),
		(wyoming , "WY"),
		#canada
		(alberta , "AB (Canada)"),
		(british_columbia , "BC (Canada)"),
		(manitoba , "MB (Canada)"),
		(new_brunswick , "NB (Canada)"),
		(newfoundland_labrador , "NL (Canada)"),
		(northwest_territories , "NT (Canada)"),
		(nova_scotia , "NS (Canada)"),
		(nunavut , "NU (Canada)"),
		(ontario , "ON (Canada)"),
		(prince_edward_island , "PE (Canada)"),
		(quebec , "QC (Canada)"),
		(saskatchewan , "SK (Canada)"),
		(yukon , "YT (Canada)")
	]