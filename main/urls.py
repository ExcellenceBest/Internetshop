from django.urls import path
from main.views import main, registration

urlpatterns = [
    path('', main),
    path('registration/', registration)
]

