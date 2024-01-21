from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.save_phone, name='save_phone'),
    path('save_phone/', views.save_phone, name='save_phone'),
    path('massage/', views.massage, name='massage'),
    path('analyzes/', views.analyzes, name='analyzes'),
    path('save_phone/', views.analyzes, name='save_phone'),
    path('sport/', views.sport, name='sport'),
    path('index/', views.index, name='index'),
]