from django.urls import path
from mapp import views

urlpatterns = [
    path('', views.mapp, name='mapp')
]