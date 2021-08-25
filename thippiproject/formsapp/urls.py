from django.urls import path
from formsapp import views

urlpatterns = [
    path('', views.check),
     path('user', views.userRegistrationForm)
]
