from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('main.urls')),
    path('basket/', include('basket.urls')),
    path('contacts/', include('contacts.urls')),
    path('catalog/', include('catalog.urls')),
]
