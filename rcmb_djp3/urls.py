from django.contrib import admin
from django.urls import path, include, re_path as url
from rcmb_app import views
from karzav import views
from invtech import views
from entry_app import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('rcmb_app.urls')),
    path('karzav/', include('karzav.urls')),
    path('invtech/', include('invtech.urls')),
    path('entry_app/', include('entry_app.urls')),
    path('authorization/', include('authorization.urls')),
    path('accounts/', include('allauth.urls')),
    path('mapp/', include('mapp.urls')),
]