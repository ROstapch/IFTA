from django.db import models
from Core.models import models
from .processing.choices import Jurisdiction_list, TimeZones_List
from django.contrib.auth.models import User



class Daily_Location(models.Model):
	truck = models.ForeignKey('Core.Unit', on_delete = models.PROTECT, help_text='Link to the related unit(vehicle) data')

	date = models.DateTimeField(help_text='Date (mm/dd/yyyy)')
	jurisdiction = models.CharField(max_length=10, choices=Jurisdiction_list.jurisdiction_choice, help_text='Jurisdiction abbreviation')
	miles = models.PositiveIntegerField(help_text='Miles at current jurisdiction')
	timezone = models.CharField(max_length=30, default = TimeZones_List.utc_5, choices=TimeZones_List.tz_choice, help_text='Timezone used when getting data')

	start_odom = models.PositiveIntegerField(null=True, blank=True, help_text='Start odometer readings')
	end_odom = models.PositiveIntegerField(null=True, blank=True, help_text='End odometer readings')

	start_lat = models.FloatField(default=0.0, null=True, blank=True, help_text='Start latitude')
	start_lon = models.FloatField(default=0.0, null=True, blank=True, help_text='Start longitude')
	end_lat = models.FloatField(default=0.0, null=True, blank=True, help_text='End latitude')
	end_lon = models.FloatField(default=0.0, null=True, blank=True, help_text='End longitude')

	previous=models.OneToOneField('self', null=True, blank=True, on_delete = models.SET_NULL, related_name="next")



class Fuel(models.Model):
	truck = models.ForeignKey('Core.Unit', on_delete = models.PROTECT, help_text='Link to the related unit(vehicle) data')
	driver = models.ForeignKey('Core.Driver', default=None,null=True, blank=True, on_delete = models.SET_DEFAULT, help_text='Link to related the driver data')

	date = models.DateTimeField(help_text='Date (mm/dd/yyyy)')
	jurisdiction = models.CharField(max_length=10, choices=Jurisdiction_list.jurisdiction_choice, help_text='Jurisdiction abbreviation')

	fuel_amount = models.FloatField(default=0.0, help_text='Volume of fuel bought')
	total_cost = models.FloatField(default=0.0, help_text='Cost of bought fuel')

	ref_no = models.CharField(max_length=15, null=True, blank=True, help_text='Invoice number')
	vendor = models.CharField(max_length=40, help_text='Truck stop name')
	



class Jurisdiction(models.Model):
	jurisdiction_name = models.CharField(max_length=10, choices=Jurisdiction_list.jurisdiction_choice, help_text='Jurisdiction abbreviation')
	miles = models.PositiveIntegerField(help_text='Total miles in jurisdiction')
	fuel = models.FloatField(default=0.0, help_text='Volume of fuel bought in jurisdiction')

	report = models.ForeignKey('Total_Report', on_delete = models.CASCADE, help_text='Link to the related report data')


class Total_Report(models.Model):
	start_date = models.DateField(help_text='Start date of the report')
	end_date = models.DateField(help_text='Ending date of the report')
	done_by = models.ForeignKey(User, default=None, null = True, blank=True, on_delete=models.SET_DEFAULT)

	truck = models.ForeignKey('Core.Unit', default=None, on_delete = models.PROTECT, help_text='Link to the related unit(vehicle) data')
	