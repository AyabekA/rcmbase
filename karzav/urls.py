from django.urls import path, re_path as url
from karzav import views

urlpatterns = [
    path('', views.karzav_list, name='karzav_list'),
    path('karzav_list/', views.KarzavListing.as_view(), name='listing'),
    path('ajax/oblasti/', views.getOblasti, name = "get_oblasti"),
    path('ajax/raiony/', views.getRaiony, name = "get_raiony"),
    path('ajax/statusy/', views.getStatus, name = "get_statusy"),
    path('ajax/nedrousers/', views.getNedrousers, name = "get_nedrousers"),
    path('karzav_card/', views.karzav_cardv, name='karzav_cardv'),
    path('fizmeh_har/', views.fizmeh_harv, name='fizmeh_harv'),
    path('fizmeh_harv/', views.fizmeh_harvv, name='fizmeh_harvv'),
    path('karzav_delete/', views.karzav_delete, name='karzav_delete'),
    path('karzav_material_delete/', views.karzav_material_delete, name='karzav_material_delete'),
]