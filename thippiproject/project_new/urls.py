from django.urls import path
from project_new import views

urlpatterns = [
    path('', views.index),
    path('electronics/', views.electronics),
    path('toys/', views.toys),
    path('shoes/', views.shoes),
]
