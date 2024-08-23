from django.urls import path
from catalog.views import main, likes

urlpatterns = [
    path('', main),
    path('/catalog/', likes),
]
