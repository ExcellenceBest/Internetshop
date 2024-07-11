from django.urls import path
from contacts.views import main

urlpatterns = [
    path('', main),
]
