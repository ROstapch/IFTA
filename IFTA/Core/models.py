from django.db import models



class Company(models.Model):
	company_id = models.IntegerField()
	company_name = models.CharField(max_length=60)
	company_api_key = models.CharField(max_length=100)


	def __str__(self):
		return self.company_name


class Unit(models.Model):
	unit_id = models.IntegerField()
	unit_number = models.IntegerField(primary_key=True)
	unit_company = models.ForeignKey('Company', on_delete = models.CASCADE)

	unit_vin = models.CharField(max_length=60)
	unit_plate = models.CharField(max_length=10)
	unit_eld = models.CharField(max_length=30)

	unit_active = models.BooleanField()
	unit_ifta = models.BooleanField()


	def __str__(self):
		return self.unit_number


class Driver(models.Model):
	driver_id = models.IntegerField()

	driver_name = models.CharField(max_length=20)
	driver_lastname = models.CharField(max_length=20)
	driver_phone = models.CharField(max_length=20)

	driver_active = models.BooleanField()


	def __str__(self):
		return ' '.join([self.driver_name, self.driver_lastname])

