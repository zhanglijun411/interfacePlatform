from django.urls import path
from apps.interface import views

urlpattern = [
    path('', views.homePage),
    path('interface_tools/', views.interfaceTools),
    path('send/', views.send)
]