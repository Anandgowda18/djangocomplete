from django.urls import path
from modelapp import views

urlpatterns = [
    path('', views.index),
    path('listproject/',views.listproject),
    path('addproject/',views.addproject),
]