from django.db import models
from Core.models import models
from .processing.choices import Jurisdiction_list, TimeZones_List
from django.contrib.auth.models import User



class Daily_Location(models.Model):
	truck = models.ForeignKey('Core.Unit', on_delete = models.PROTECT, help_text='Link to the related unit(vehicle) data')

	date = models.DateField(help_text='Date (mm/dd/yyyy)') #convert to yyyy-mm-dd when saving
	jurisdiction = models.CharField(max_length=10, choices=Jurisdiction_list.jurisdiction_choice, help_text='Jurisdiction abbreviation')
	miles = models.PositiveIntegerField(help_text='Miles at current jurisdiction')
	timezone = models.CharField(max_length=30, default = TimeZones_List.utc_5, choices=TimeZones_List.tz_choice, help_text='Timezone used when getting data')

	start_odom = models.PositiveIntegerField(null=True, blank=True, help_text='Start odometer readings')
	end_odom = models.PositiveIntegerField(null=True, blank=True, help_text='End odometer readings')

	start_lat = models.FloatField(default=0.0, null=True, blank=True, editable=False, help_text='Start latitude')
	start_lon = models.FloatField(default=0.0, null=True, blank=True, editable=False, help_text='Start longitude')
	end_lat = models.FloatField(default=0.0, null=True, blank=True, editable=False, help_text='End latitude')
	end_lon = models.FloatField(default=0.0, null=True, blank=True, editable=False, help_text='End longitude')

	previous = models.OneToOneField('self', null=True, blank=True, editable=False, on_delete = models.SET_NULL, related_name="next")
	chained = models.BooleanField(default=False, editable=False)




	def __str__(self):
		return str(self.jurisdiction)



	def create(self, unit, date, location, miles):
		self.truck = unit
		self.date = date
		self.jurisdiction = location
		self.miles = miles




	def is_last(self):
		try:
			return self.next is None
		except Daily_Location.DoesNotExist:
			return True

	
	def delete(self):
		#if location is not the last node
		if not Daily_Location.is_last(self):
			temp_next = self.next
			temp_prev = self.previous
			super(Daily_Location, self).delete()
			temp_next.previous = temp_prev
			temp_next.save()
		else:
			temp_prev = self.previous
			#if location is last node
			if temp_prev:
				super(Daily_Location, self).delete()
				temp_prev.next = None
			#location is the only node
			else:
				super(Daily_Location, self).delete()


	def truck_last_node(unit):
		if Daily_Location.objects.all().filter(truck = unit).filter(chained = True):
			nodes_amount = len(Daily_Location.objects.all().filter(truck = unit).filter(chained = True))
			last_node = Daily_Location.objects.all().filter(truck = unit).filter(chained = True)[0]
			while not last_node.is_last():
				last_node = last_node.next
			return last_node
		else:
			return None


	def append_node(self):
		last_node = Daily_Location.truck_last_node(self.truck)
		self.previous = last_node
		self.chained = True
		self.save()

	#ordered location list, where first element is the latest location, and the last element is the newest location
	def append_nodes(unit, location_list): 
		last_node = Daily_Location.truck_last_node(unit)
		for node in location_list:
			node.previous = last_node
			node.chained = True
			node.save()
			last_node = node









class Fuel(models.Model):
	truck = models.ForeignKey('Core.Unit', on_delete = models.PROTECT, help_text='Link to the related unit(vehicle) data')
	driver = models.ForeignKey('Core.Driver', default=None,null=True, blank=True, on_delete = models.SET_DEFAULT, help_text='Link to related the driver data')

	date = models.DateField(help_text='Date (mm/dd/yyyy)') #convert to yyyy-mm-dd when saving
	jurisdiction = models.CharField(max_length=10, choices=Jurisdiction_list.jurisdiction_choice, help_text='Jurisdiction abbreviation')

	fuel_amount = models.FloatField(default=0.0, help_text='Volume of fuel bought')
	total_cost = models.FloatField(default=0.0, help_text='Cost of bought fuel')

	ref_no = models.CharField(max_length=15, null=True, blank=True, help_text='Invoice number')
	vendor = models.CharField(max_length=40, help_text='Truck stop name')


	def __str__(self):
		return str(self.fuel_amount)




class Jurisdiction(models.Model):
	jurisdiction_name = models.CharField(max_length=10, choices=Jurisdiction_list.jurisdiction_choice, help_text='Jurisdiction abbreviation')
	miles = models.PositiveIntegerField(help_text='Total miles in jurisdiction')
	fuel = models.FloatField(default=0.0, help_text='Volume of fuel bought in jurisdiction')

	report = models.ForeignKey('Total_Report', on_delete = models.CASCADE, help_text='Link to the related report data')


	def __str__(self):
		return str(self.jurisdiction_name)


class Total_Report(models.Model):
	start_date = models.DateField(help_text='Start date of the report (mm/dd/yyyy)') #convert to yyyy-mm-dd when saving
	end_date = models.DateField(help_text='Ending date of the report (mm/dd/yyyy)') #convert to yyyy-mm-dd when saving
	done_by = models.ForeignKey(User, default=None, null = True, blank=True, on_delete=models.SET_DEFAULT)

	truck = models.ForeignKey('Core.Unit', default=None, on_delete = models.PROTECT, help_text='Link to the related unit(vehicle) data')
	