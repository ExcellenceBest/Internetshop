from django.urls import path
from basket.views import main


urlpatterns = [
    path('', main)
]
