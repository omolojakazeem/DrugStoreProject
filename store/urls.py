from django.urls import path, include
from django.contrib import admin
from .views import home_view

app_name = 'store'

urlpatterns = [
    path('',home_view, name = 'home')
]