from django.shortcuts import render

# Create your views here.
def thirdindex(request):
    mydict = {"name":'Anand'}
    return render(request,'thirdapp/index.html',mydict)

def emp(request):
    empdict = {'id':1,'name':"employee",'sal':'10000'}
    return render(request,'thirdapp/employee.html',empdict)