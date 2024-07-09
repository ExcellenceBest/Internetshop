from django.urls import path
from catalog.views import main

urlpatterns = [
    path('catalog/', main)
]
