from django.urls import path
from basket.views import main, search_product, in_basket


urlpatterns = [
    path('', main),
    path('basket/search_product/', search_product),
    path('basket/in_basket/', in_basket)
]
