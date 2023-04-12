from django.urls import path
from apps.interface import views

urlpattern = [
    path('', views.homePage, name='home'),
    path('interface_tools/', views.interfaceTools, name='tools'),
    path('send/', views.send, name='send'),
]