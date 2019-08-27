

class Location():
	jurisdiction_name = ""
	start_odometer = 0
	end_odometer = 0
	miles = 0
	start_lat = 0.0
	start_lon = 0.0
	end_lat = 0.0
	end_lon = 0.0

	def __str__(self):
		return self.jurisdiction_name



class Daily_Locations():
	date = None #handle convertion from yyyy-mm-dd to  mm/dd/yyyy 
	locations = []

	start_odometer = 0
	end_odometer = 0
	miles = 0

	truck = 0
	driver = ""