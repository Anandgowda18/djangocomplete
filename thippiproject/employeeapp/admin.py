from django.contrib import admin
from employeeapp.models import employee
# Register your models here.

class employeedetails(admin.ModelAdmin):
    list_display = ['firstname','lastname','salary','email']
admin.site.register(employee,employeedetails)