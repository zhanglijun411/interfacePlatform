from django.urls import path
from apps.interface import views

urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('interface/', views.interfaceTools, name='interface_tools')
]