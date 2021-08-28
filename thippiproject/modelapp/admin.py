from django.contrib import admin
from modelapp.models import Project
# Register your models here.

class Projectadmin(admin.ModelAdmin):
    list_display = ['startdate','enddate','name','assignedto','priority']

admin.site.register(Project,Projectadmin)