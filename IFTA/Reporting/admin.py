from django.contrib import admin
from .models import *

class JurisdictionInline(admin.TabularInline):
	model = Jurisdiction
	extra = 1

class Total_Report_Admin(admin.ModelAdmin):
    inlines = [JurisdictionInline]


admin.site.register(Total_Report, Total_Report_Admin)
