from django.urls import path, include
from .views import *
urlpatterns = [
    path('temp/',getTemp),
    path('light/',getLight),
    path('alert/',getALert)
]
