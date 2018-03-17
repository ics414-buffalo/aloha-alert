from django.urls import path, re_path
from . import views

app_name = 'alertsystem'
urlpatterns = [
    path('', views.index, name='index'),
    path('foreign/', views.foreign, name='foreign')
]