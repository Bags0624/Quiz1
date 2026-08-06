from django.urls import path
from .views import inquiry_create_view
from django.shortcuts import render

urlpatterns = [
    path('inquiry/', inquiry_create_view, name='inquiry_create'),
    path('inquiry/success/', 
         lambda request: render(request, 'success.html'), 
         name='inquiry_success'),
]