from django.urls import path
from employeeapp import views

urlpatterns = [
    path('', views.employeedata),
]
