"""DapengBay URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include,re_path
from . import views



urlpatterns = [
    path('home/', views.home, name='home'),
    path('list/', views.list_persons, name='list_persons'),
    path('add_person/', views.add_person, name='add_person'),
    path('delete_person/<int:person_id>/', views.delete_person, name='delete_person'),
    path('update/', views.update_person, name='update_person'),
    #path('', views.login, name='login'),
    #path('register/', views.register, name='register')
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('complete/', views.complete, name='complete'),
    path('edit/', views.edit1, name='edit'),
    path('logout/', views.logout, name='logout'),
]


