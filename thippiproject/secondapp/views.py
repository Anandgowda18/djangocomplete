from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def greet(request):
    return HttpResponse('<h1>welcome to second page</h1>')