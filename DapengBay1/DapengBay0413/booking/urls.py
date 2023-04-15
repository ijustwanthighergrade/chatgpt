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
from booking import views
import booking


urlpatterns = [
    # path('save/', views.save_appointment),
    # path('success/',views.appointment_success),
    path('reserve/',views.reserve,name='reserve'),
    path('news/',views.news,name='news'),
    path('save/',views.save_travel, name='save_travel'),
    path('checkout/',views.checkout,name='checkout'),
    path('index/',views.index,name='index'),
    path('book_c/',views.book_c, name='book_c'),
    path('part_d/', views.submit_form, name='participate_form'),

    path('dinner/', views.show_dinner, name='dinner'),
    path('snacks/', views.show_dinner_snacks, name='dinner1'),
    path('noodles/', views.show_dinner_noodles, name='dinner2'),
    path('hotdishes/', views.show_dinner_hotdishes, name='dinner3'),
    path('submit_order/',views.submit_order, name='submit_order'),
    path('submit_order2/', views.submit_order2, name='submit_order2'),
    path('break/', views.show_break, name='break'),
]


