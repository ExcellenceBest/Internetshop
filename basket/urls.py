from django.urls import path
from basket.views import main, search_product


urlpatterns = [
    path('', main),
    path('basket/search_product/', search_product),
]
