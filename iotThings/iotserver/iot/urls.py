from django.urls import path
from .views import Home,api_test
urlpatterns = [
    path("",Home),
    path('api_test',api_test)
]