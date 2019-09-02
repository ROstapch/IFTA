from django.contrib import admin
from .models import *



class UnitsInline(admin.TabularInline):
	model = Unit
	extra = 1

class CompanyAdmin(admin.ModelAdmin):
	inlines = [UnitsInline]
	list_display = ('company_name', 'amount_of_units')


class UnitAdmin(admin.ModelAdmin):
	list_display = ('unit_number', 'company', 'unit_active')


class DriverAdmin(admin.ModelAdmin):
	list_display = ('full_name', 'driver_phone', 'driver_status')



admin.site.register(Company, CompanyAdmin)
admin.site.register(Unit, UnitAdmin)
admin.site.register(Driver, DriverAdmin)
