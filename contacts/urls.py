from django.urls import path
from contacts.views import main, comment

urlpatterns = [
    path('', main),
    path('comment/', comment),
]
