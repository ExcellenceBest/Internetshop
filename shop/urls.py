from django.contrib import admin
from django.urls import path, re_path, include
import about.views
import basket.views
import catalog.views
import contacts.views
import main.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main.views.main),
    path('registration/', main.views.registration),
    path('registration/registr/', main.views.registr),
    path('catalog/likes/', catalog.views.likes),
    re_path('basket/search_product/\S*', basket.views.search_product),
    path('basket/in_basket/', basket.views.in_basket),
    path('basket/basket_all/off_basket/', basket.views.off_basket),
    path('basket/basket_all/', basket.views.basket_all),
    path('main/', include('main.urls')),
    path('basket/', include('basket.urls')),
    path('contacts/', include('contacts.urls')),
    path('catalog/', include('catalog.urls')),
    path('about/', include('about.urls')),
    re_path(r'^main/', main.views.redirect),
    re_path(r'^catalog/', catalog.views.redirect),
    re_path(r'^basket/', basket.views.redirect),
    re_path(r'^contacts/', contacts.views.redirect),
    re_path(r'^about/', about.views.redirect),
]
