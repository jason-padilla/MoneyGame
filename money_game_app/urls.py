from django.urls import path     
from . import views


urlpatterns = [
    path('', views.index),
    path('clear', views.clear),
    path('process_money', views.process_money),	
]