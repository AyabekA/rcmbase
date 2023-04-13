from django.urls import path
from invtech import views


urlpatterns = [
    path('', views.invtech_list, name='invtech_list'),
    path('invtech_list/', views.InvtechListing.as_view(), name='itlisting'),
    path('ajax/technologies/', views.getTechnologies, name = "get_technologies"),
    path('ajax/statusy/', views.getStatus, name = "get_statusy"),
    path('ajax/usingareas/', views.getUsingareas, name = "get_usingareas"),
    path('ajax/providers/', views.getProviders, name = "get_providers"),
    path('ajax/producers/', views.getProducers, name = "get_producers"),
    path('invtech_info/', views.invtech_infov, name='invtech_infov'),
    path('invtech_delete/', views.invtech_delete, name='invtech_delete'),
]