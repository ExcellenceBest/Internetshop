from django.urls import path
from basket.views import main, search_product, in_basket, basket_all, off_basket


urlpatterns = [
    path('', main),
    path('basket/search_product/<str:search_product>/', search_product),
    path('basket/in_basket/', in_basket),
    path('basket/basket_all/', basket_all),
    path('basket/basket_all/off_basket/', off_basket),

]
