from django.urls import path
from rcmb_app import views

urlpatterns = [
    path('', views.title, name='title')
]