#from django.contrib import admin
from django.urls import path

from . import views
urlpatterns = [
    path('', views.list_job),
    path('', views.list_details),
]
