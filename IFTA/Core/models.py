from django.db import models



class Company(models.Model):
	company_id = models.IntegerField()
	company_name = models.CharField(max_length=60)
	__company_api_key = None


	def __str__(self):
		return self.company_name


class Unit(models.Model):
	unit_id = models.IntegerField(help_text="Unit's id in KeepTruckin system")
	unit_number = models.IntegerField(primary_key=True, help_text='Internal number of the truck in the company')
	unit_company = models.ForeignKey('Company', on_delete = models.CASCADE, help_text='Links to the company, unit belongs to')

	unit_vin = models.CharField(max_length=60, help_text='Vin number of the unit')
	unit_plate = models.CharField(max_length=10, help_text='Plate numer of the unit')
	unit_eld = models.CharField(max_length=30, help_text='Id of the ELD device installed on the unit')

	unit_active = models.BooleanField(help_text='Indicates if the unit is used by the company')
	unit_ifta = models.BooleanField(help_text='Indicates if the unit is IFTA convenient')


	def __str__(self):
		return self.unit_number


class Driver(models.Model):
	driver_id = models.IntegerField(help_text="Driver's id in KeepTruckin system")

	driver_name = models.CharField(max_length=20, help_text='Name of the driver')
	driver_lastname = models.CharField(max_length=20, help_text='Last name of the driver')
	driver_phone = models.CharField(max_length=20, help_text="Driver's phone number")

	driver_active = models.BooleanField(help_text='Indicates if the driver is working at the company')


	def __str__(self):
		return ' '.join([self.driver_name, self.driver_lastname])

