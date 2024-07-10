from django.urls import path
from main.views import main, registration

urlpatterns = [
    path('main/', main),
    path('main/registration/', registration)
]

