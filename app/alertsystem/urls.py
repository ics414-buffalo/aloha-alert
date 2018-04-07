from django.urls import path, re_path
from . import views

app_name = 'alertsystem'
urlpatterns = [
    path('', views.index, name='index'),
    # Foreign Missile Paths
    path('foreign/', views.foreign, name='foreign'),
    path('foreign/real/', views.real_foreign, name='real_foreign'),
    path('foreign/real/sent/', views.real_foreign_sent, name='real_foreign_sent'),
    path('foreign/test/', views.test_foreign, name='test_foreign'),
    path('foreign/test/sent', views.test_foreign_sent, name='test_foreign_sent'),
]