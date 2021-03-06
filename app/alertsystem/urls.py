from django.urls import path
from . import views

app_name = 'alertsystem'
urlpatterns = [
    # Home Page
    path('', views.index, name='index'),

    # Amber Alert URLs
    path('amber/', views.amber, name='amber'),
    path('amber/real/', views.real_amber, name='real_amber'),
    path('amber/real/sent/<int:amber_alert_id>', views.real_amber_sent, name='real_amber_sent'),
    path('amber/test/', views.test_amber, name='test_amber'),
    path('amber/test/sent/<int:amber_alert_id>', views.test_amber_sent, name='test_amber_sent'),

    # Natural Disaster URLs
    path('natural/', views.natural, name='natural'),
    path('natural/tsunami/', views.tsunami, name='tsunami'),
    path('natural/tsunami/real/', views.real_tsunami, name='real_tsunami'),
    path('natural/tsunami/real/sent/', views.real_tsunami_sent, name='real_tsunami_sent'),
    path('natural/tsunami/test/', views.test_tsunami, name='test_tsunami'),
    path('natural/tsunami/test/sent/', views.test_tsunami_sent, name='test_tsunami_sent'),
    path('natural/hurricane/', views.hurricane, name='hurricane'),
    path('natural/hurricane/real/', views.real_hurricane, name='real_hurricane'),
    path('natural/hurricane/real/sent/', views.real_hurricane_sent, name='real_hurricane_sent'),
    path('natural/hurricane/test/', views.test_hurricane, name='test_hurricane'),
    path('natural/hurricane/test/sent/', views.test_hurricane_sent, name='test_hurricane_sent'),

    # Foreign Missile URLs
    path('foreign/', views.foreign, name='foreign'),
    path('foreign/real/', views.real_foreign, name='real_foreign'),
    path('foreign/real/sent/', views.real_foreign_sent, name='real_foreign_sent'),
    path('foreign/test/', views.test_foreign, name='test_foreign'),
    path('foreign/test/sent/', views.test_foreign_sent, name='test_foreign_sent'),
]