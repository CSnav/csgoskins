"""csgo_supply URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('details/gun/list/', views.gunList, name='gun-list'),
    path('details/gun/<str:skinid>/', views.gunDetails, name='gun-details'),
    path('details/knife/list/', views.knifeList, name='knife-list'),
    path('details/knife/<str:skinid>/', views.knifeDetails, name='knife-details'),
    path('details/glove/list/', views.gloveList, name='glove-list'),
    path('details/glove/<str:skinid>/', views.gloveDetails, name='glove-details'),
    path('list/<int:pk>/', views.List, name='list'),
    path('list/', views.CreateList, name='list-form')
]
