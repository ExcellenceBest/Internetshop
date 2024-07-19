from django.urls import path
from about.views import main

urlpatterns = [
    path('', main),

]

