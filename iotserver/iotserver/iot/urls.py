from django.urls import path
from .views import Home, api_test

urlpatterns = [
    path('',Home),
    path('apitest',api_test)
]