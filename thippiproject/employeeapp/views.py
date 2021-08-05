from django.shortcuts import render
from employeeapp.models import employee
# Create your views here.
def employeedata(request):
    employeedetails = employee.objects.all()
    mydict = {'employeedetails':employeedetails}
    return render(request,'employeeapp/employeepage.html',mydict)