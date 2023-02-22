from django.urls import path
from apps.interface import views

urlpatterns = [
    path('tools/', views.interfaceTools, name='interfaceTools'),
]