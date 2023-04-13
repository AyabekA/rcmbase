from django.urls import path
from . import views
from .views import verify_email

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='profile'),
    path('my_publication/', views.mypublication, name='mypublication'),
    path('my_application/', views.myapplication, name='myapplication'),

    path('register/', views.register, name='register'),
    path('login_user', views.login_user, name='login_user'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('verify_email/<uuid:token>/', verify_email, name='verify_email'),
    path('complete_registration/', views.complete_registration, name='complete_registration'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('password_reset/', views.password_reset, name='password_reset'),
    path('password_reset_done/', views.password_reset_done, name='password_reset_done'),
    path('password_reset_confirm/<uuid:token>/', views.password_reset_confirm, name='password_reset_confirm'),
    path('password_reset_complete/', views.password_reset_complete, name='password_reset_complete'),
    path('list_admin/', views.list_admin, name="list_admin"),
    path('list_projector/', views.list_projector, name="list_projector"),
    path('list_provider/', views.list_provider, name="list_provider"),
    path('create_user/', views.create_user, name="create_user"),
    path('delete_user/', views.delete_user, name="delete_user"),
]
