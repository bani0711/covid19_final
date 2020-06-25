# config.urls.py
from django.contrib import admin
from django.urls import path
from chart import views

urlpatterns = [
    path('', views.home, name='home'),
    path('covid19/',
         views.covid19, name='covid19')
]