from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def greet(request):
    return HttpResponse('<h1>Hello welcome to firt page</h>')
from datetime import datetime
def dt(request):
    date_time = datetime.now()
    return HttpResponse(date_time)