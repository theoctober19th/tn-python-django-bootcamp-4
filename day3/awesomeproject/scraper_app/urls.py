
from django.contrib import admin
from django.urls import path

from scraper_app.views import index

urlpatterns = [
    path('index/', index)
]
