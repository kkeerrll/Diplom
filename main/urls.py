from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.save_phone, name='save_phone'),
    path('save_phone/', views.save_phone, name='save_phone'),
    path('Massage.html', views.massage, name='massage'),
    path('Analyzes.html', views.analyzes, name='analyzes'),
    path('Sport.html', views.sport, name='sport'),
    path('index.html', views.index, name='index'),

]