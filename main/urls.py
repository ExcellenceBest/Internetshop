from django.urls import path
from main.views import main, registration, registr

urlpatterns = [
    path('', main),
    path('registration/', registration),
    path('registration/registr/', registr),
]

