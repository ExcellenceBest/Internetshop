from django.contrib import admin
from django.urls import path, include

import basket.views
import catalog.views
import contacts.views
import main.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', main.views.main),
    path('basket/', basket.views.main),
    path('contacts/', contacts.views.main),
    path('catalog/', catalog.views.main),
]
