from django.db import models
from django.contrib.auth.models import User
from .processing.choices import *



class Company(models.Model):
	company_id = models.IntegerField(unique=True, editable=False, null=True)
	company_name = models.CharField(max_length=60)
	company_address = models.CharField(max_length=250, null=True, blank=True)


	def __str__(self):
		return self.company_name

	def amount_of_units(self):
		return self.unit_set.count()

	units = property(amount_of_units)

	class Meta:
		verbose_name = 'Company'
		verbose_name_plural = "Companies"



class Unit(models.Model):
	unit_id = models.IntegerField(editable=False ,unique=True, null=True, help_text="Unit's id in KeepTruckin system")
	unit_number = models.IntegerField(unique=True, help_text='Internal number of the truck in the company')
	unit_company = models.ForeignKey('Company', on_delete = models.CASCADE, help_text='Links to the company, unit belongs to')

	unit_eld = models.CharField(default=None, max_length=30, null = True, blank=True, help_text='Id of the ELD device installed on the unit')

	unit_gross_weight = models.IntegerField(null = True, blank=True, help_text='Gross weight of the truck')

	unit_active = models.BooleanField(default=False, help_text='Indicates if the unit is used by the company')
	unit_ifta = models.BooleanField(default=True, help_text='Indicates if the unit is IFTA convenient (gross weight 26000 pounds or more)')

	unit_staff = models.ForeignKey(User,default=None, null = True, blank=True, on_delete=models.DO_NOTHING)
	unit_type = models.CharField(default=None, max_length=30, null = True, blank=True, choices=Unit_Groups.unit_group_choice, help_text='Group of units')

	def __str__(self):
		return str(self.unit_number)

	def company(self):
		return self.unit_company



class Driver(models.Model):
	driver_id = models.IntegerField(editable=False ,unique=True, null=True,help_text="Driver's id in KeepTruckin system")

	driver_name = models.CharField(max_length=20, help_text='Name of the driver')
	driver_lastname = models.CharField(max_length=20, help_text='Last name of the driver')
	driver_phone = models.CharField(max_length=20, null=True, help_text="Driver's phone number")
	driver_email = models.EmailField(max_length=250, null=True, help_text="Driver's e-mail address")

	driver_status = models.BooleanField(default=False, help_text='Indicates if the driver is working at the company')


	def __str__(self):
		return ' '.join([self.driver_name, self.driver_lastname])

	def full_name(self):
		return ' '.join([self.driver_name, self.driver_lastname])

