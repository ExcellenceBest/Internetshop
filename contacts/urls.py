from django.urls import path
from contacts.views import main

urlpatterns = [
    path('contacts/', main),
]
