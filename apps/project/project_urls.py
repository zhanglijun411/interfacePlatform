from django.urls import path
from apps.project import views

urlpatterns = [
    path('', views.projectView, name='pro'),
    path('needs/page=<int:page>', views.needsView, name='needs'),
    # path('needs/category/', views.needCategoryView, name='needCategory')
]