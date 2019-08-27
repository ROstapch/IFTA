from django.contrib import admin
from .models import Company, Unit



class UnitsInline(admin.TabularInline):
	model = Unit
	extra = 1

class CompanyAdmin(admin.ModelAdmin):
	inlines = [UnitsInline]
	list_display = ('company_name', 'amount_of_units')


class UnitAdmin(admin.ModelAdmin):
	list_display = ('unit_number', 'company')


admin.site.register(Company, CompanyAdmin)
admin.site.register(Unit, UnitAdmin)
