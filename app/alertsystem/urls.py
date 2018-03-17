from django.urls import path, re_path
from . import views

app_name = 'alertsystem'
urlpatterns = [
    path('', views.index, name='index'),
    path('foreign/', views.foreign, name='foreign'),
    path('foreign/real/', views.real_foreign, name='real_foreign'),
    path('foreign/real/sent/', views.real_foreign_sent, name='real_foreign_sent')
]