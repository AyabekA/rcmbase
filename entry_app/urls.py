from django.urls import path
from entry_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.entappv, name='entapp_form'),
    path('entapp_edit/', views.entappv_edit, name='entapp_edit'),
    path('entapp_list/', views.entapp_list, name="entapp_list"),
    path('entapp_listt/', views.EntappListing.as_view(), name='ealisting'),
    path('ajax/sent_status/', views.getSentStatus, name = "get_sent_status"),
    path('ajax/entapp_status/', views.getEntappStatus, name = "get_entapp_status"),
    path('entapp_invtech/', views.entapp_invtech, name='entapp_invtech'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)