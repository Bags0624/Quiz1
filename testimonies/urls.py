from django.urls import path
from . import views

urlpatterns = [
    path('', views.testimony_list, name='testimony_list'),
    path('<int:pk>/', views.testimony_detail, name='testimony_detail'),
    path('create/', views.testimony_create_view, name='testimony_create'),
]