

class StatesConnected(object):
	__states_list = {
		"WA" : ["WA", "OR", "ID", "BC"],
		"OR" : ["OR", "WA", "ID", "NV", "CA"],
		"CA" : ["CA", "OR", "nv", "AZ"],
		"ID" : ["ID", "MT", "WY", "UT", "NV", "OR", "WA", "BC"],
		"NV" : ["NV", "ID", "UT", "AZ", "CA", "OR"],
		"AZ" : ["AZ", "UT", "NM", "CA", "NV"], #CO
		"MT" : ["MT", "ND", "SD", "WY", "ID", "BC", "AB", "SK"],
		"WY" : ["WY", "MT", "SD", "NE", "CO", "UT", "ID"],
		"UT" : ["UT", "ID", "WY", "CO", "AZ", "NV"], #NM
		"CO" : ["CO", "WY", "NE", "KS", "OK", "NM", "UT"], #AZ
		"NM" : ["NM", "CO", "OK", "TX", "AZ"], #UT
		"ND" : ["ND", "MN", "SD", "MT", "SK", "MD"],
		"SD" : ["SD", "ND", "MN", "IA", "NE", "WY", "MT"],
		"NE" : ["NE", "SD", "IA", "MO", "KS", "CO", "WY"],
		"KS" : ["KS", "NE", "MO", "OK", "CO"],
		"OK" : ["OK", "KS", "MO", "AR", "TX", "NM", "CO"],
		"TX" : ["TX", "OK", "AR", "LA", "NM"],
		"MN" : ["MN", "WI", "IA", "SD", "ND", "MB", "ON"],
		"IA" : ["IA", "MN", "WI", "IL", "MO", "NE", "SD"],
		"MO" : ["MO", "IA", "IL", "KY", "TN", "AR", "OK", "KS", "NE"],
		"AR" : ["AR", "MO", "TN", "MS", "LA", "TX", "OK"],
		"LA" : ["LA", "AR", "MS", "TX"],
		"WI" : ["WI", "MI", "IL", "IA", "MN"],
		"IL" : ["IL", "WI", "IN", "KY", "MO", "IA"],
		"KY" : ["KY", "IN", "OH", "WV", "VA", "TN", "MO", "IL"],
		"IN" : ["IN", "MI", "OH", "KY", "IL"],
		"MI" : ["MI", "WI", "IN", "OH", "ON"],
		"OH" : ["OH", "PA", "WV", "KY", "IN", "MI"],
		"WV" : ["WV", "PA", "VA", "KY", "MD", "OH"],
		"VA" : ["VA", "NC", "TN", "WV", "KY", "MD"],
		"PA" : ["PA", "NY", "OH", "WV", "DE", "MD", "NJ"],
		"NY" : ["NY", "PA", "VT", "CT", "MA", "NJ", "ON", "QC"],
		"MS" : ["MS", "TN", "AL", "LA", "AR"],
		"AL" : ["AL", "TN", "GA", "FL", "MS"],
		"TN" : ["TN", "KY", "VA", "NC", "GA", "AL", "MS", "AR", "MO"],
		"NC" : ["NC", "VA", "SC", "GA", "TN"],
		"SC" : ["SC", "NC", "GA"],
		"GA" : ["GA", "TN", "NC", "SC", "FL", "AL"],
		"FL" : ["FL", "GA", "AL"],
		"CT" : ["CT", "NY", "RI", "MA"],
		"DE" : ["DE", "NJ", "PA", "MD"],
		"ME" : ["ME", "NH", "QC", "NB"],
		"MD" : ["MD", "VA", "WV", "DE", "PA"],
		"MA" : ["MA", "NY", "RI", "VT", "CT", "NH"],
		"NH" : ["NH", "VT", "ME", "MA", "QC"],
		"NJ" : ["NJ", "PA", "DE", "NY"],
		"RI" : ["RI", "MA", "CT"],
		"VT" : ["VT", "NH", "NY", "MA", "QC"],
		"AK" : ["AK", "BC", "YT"]
		}


	def check(self, current_jurisdiction = "", next_jurisdiction = ""):
		try:
			check = next_jurisdiction in self.__states_list[current_jurisdiction]
			return (check)
		except KeyError:
			return None

