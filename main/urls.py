from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('bd', views.bd, name='bd'),
    path('create', views.create, name='create'),
]