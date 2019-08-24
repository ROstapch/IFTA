from django.db import models
from Core.models import Unit, Driver, Company
from .choices import Fuel_Types, Volume_Measures, Distance_Measures, Currency_Types


class Location(models.Model):
	jurisdiction_name = models.CharField(max_length=10, help_text='Jurisdiction abbreviation')

	start_odometer = models.PositiveIntegerField(help_text="Odometer reading when entering jurisdiction")
	end_odometer = models.PositiveIntegerField(help_text="Odometer reading when exiting jurisdiction")
	miles = models.PositiveIntegerField(help_text='Total miles in jurisdiction according to Keep Trucking data')	#important

	location_date = models.ForeignKey('Daily_Locations', on_delete = models.CASCADE, help_text='Link to a related date')



class Daily_Locations(models.Model):
	date = models.DateField(help_text='Date (mm-dd-yyyy)')	#handle convertion

	start_odometer = models.PositiveIntegerField(help_text="Odometer reading on the start of the day")
	end_odometer = models.PositiveIntegerField(help_text="Odometer reading on the end of the day")
	miles = models.PositiveIntegerField(help_text='Total miles this day according to odometers difference')	#important

	truck = models.ForeignKey('Core.Unit', on_delete = models.DO_NOTHING, help_text='Link to the related unit(vehicle) data')
	driver = models.ForeignKey('Core.Driver', on_delete = models.DO_NOTHING, help_text='Link to related the driver data')



class Fuel(models.Model):
	truck = models.ForeignKey('Core.Unit', on_delete = models.DO_NOTHING, help_text='Link to the related unit(vehicle) data')
	driver = models.ForeignKey('Core.Driver', on_delete = models.DO_NOTHING, help_text='Link to related the driver data')

	date = models.DateTimeField(help_text='Date (mm-dd-yyyy)')	#handle convertion
	jurisdiction = models.CharField(max_length=10, help_text='Jurisdiction abbreviation')

	fuel_type = models.CharField(max_length=20, choices=Fuel_Types.fuel_choice, default='diesel', help_text='Fuel type (diesel by default)')

	total_cost = models.FloatField(help_text='Cost of bought fuel')
	currency = models.CharField(max_length=5,choices=Currency_Types.currency_choice, default='USD', help_text='Currency (US dollar by default)')
	fuel_amount = models.FloatField(help_text='Volume of fuel bought')
	fuel_unit = models.CharField(max_length=10, choices=Volume_Measures.volume_choice, default='gal', help_text='Volume measurement (gallons by default)')

	ref_no = models.CharField(max_length=15, blank=True, help_text='Invoice number')
	vendor = models.CharField(max_length=40, help_text='Truck stop name')

	odometer = models.IntegerField(blank=True, help_text='Odometer reading on arrival to the truck stop')
	odometer_unit = models.CharField(max_length=5, choices=Distance_Measures.distance_choice, blank=True, help_text='Distance measurement')



class Jurisdiction(models.Model):
	jurisdiction_name = models.CharField(max_length=10, help_text='Jurisdiction abbreviation')
	miles = models.PositiveIntegerField(help_text='Total miles in jurisdiction')

	report = models.ForeignKey('Total_Report', on_delete = models.CASCADE, help_text='Link to the related report data')



class Total_Report(models.Model):
	start_date = models.DateField(help_text='Start date of the report')
	end_date = models.DateField(help_text='Ending date of the report')

