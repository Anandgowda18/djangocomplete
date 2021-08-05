from django.urls import path
from thirdapp import views

urlpatterns = [
    path('', views.thirdindex),
    path('empurl', views.emp),
]
