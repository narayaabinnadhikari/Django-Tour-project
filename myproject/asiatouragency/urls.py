from django.urls import path
from . import views


#Defining a list of URL patterns

urlpatterns = [
    path('', views.index)
]
