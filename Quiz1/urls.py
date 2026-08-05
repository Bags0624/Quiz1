"""
URL configuration for Quiz1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from portfolio import views as portfolio_views
from testimonies import views as testimony_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', portfolio_views.project_list, name='homepage'), 
    path('projects/', portfolio_views.project_list, name='project_list'),
    path('projects/<int:pk>/', portfolio_views.project_detail, name='project_detail'),
    path('testimonies/', testimony_views.testimony_list, name='testimony_list'),
    path('testimonies/<int:pk>/', testimony_views.testimony_detail, name='testimony_detail'),
]