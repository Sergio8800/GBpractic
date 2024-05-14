
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_app, name='index_app'),
    path('about/', views.about, name='about'),
]
