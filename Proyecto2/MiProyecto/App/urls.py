
from django.contrib import admin
from django.urls import path
from .views import show_index

urlpatterns = [
    path('', show_index)
]