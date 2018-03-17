from django.urls import path
from . import views

app_name = 'alertsystem'
urlpatterns = [
    path('', views.index, name='index'),
]