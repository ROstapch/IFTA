from django.db import models
from Core.models import Unit, Driver, Company


class Location(models.Model):
	jurisdiction_name = models.CharField(max_length=5)

	start_odometer = models.PositiveIntegerField()
	end_odometer = models.PositiveIntegerField()
	miles = models.PositiveIntegerField()

	location_date = models.ForeignKey('Daily_Location', on_delete = models.CASCADE)



class Daily_Location(models.Model):
	date = models.DateField()

	start_odometer = models.PositiveIntegerField()
	end_odometer = models.PositiveIntegerField()
	miles = models.PositiveIntegerField()

	truck = models.ForeignKey('Core.Unit', on_delete = models.DO_NOTHING)
	driver = models.ForeignKey('Core.Driver', on_delete = models.DO_NOTHING)



class Fuel(models.Model):
	truck = models.ForeignKey('Core.Unit', on_delete = models.DO_NOTHING)
	driver = models.ForeignKey('Core.Driver', on_delete = models.DO_NOTHING)

	date = models.DateTimeField()
	jurisdiction = models.CharField(max_length=20)

	fuel_type = models.CharField(max_length=20, default='diesel')

	total_cost = models.FloatField()
	currency = models.CharField(max_length=5, default='ULSD')
	fuel_amount = models.FloatField()
	fuel_unit = models.CharField(max_length=10, default='gal')

	ref_no = models.CharField(max_length=15, blank=True)
	vendor = models.CharField(max_length=40)

	odometer = models.IntegerField(blank=True)
	odometer_unit = models.CharField(max_length=5, blank=True)



def save_report_dir(instance, filename):
	return 'reports/%Y/%m/%d/{0}_%H:%M'.format(filename)

class Total_Report(models.Model):
	start_date = models.DateField()
	end_date = models.DateField()
	report = models.FileField(upload_to=save_report_dir,max_length=100)


