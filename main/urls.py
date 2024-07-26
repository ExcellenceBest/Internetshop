from django.urls import path
from main.views import main, registration, registr
from catalog.views import likes

urlpatterns = [
    path('', main),
    path('registration/', registration),
    path('registration/registr/', registr),
    path('catalog/likes/', likes)
]

