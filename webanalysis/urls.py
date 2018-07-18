from django.urls import path
from webanalysis import views

app_name = 'webanalysis'

urlpatterns = [
    path('', views.index, name="index"),
    path('upload/', views.upload, name="upload"),
    path('pie_data/', views.pie_data, name="pie_data"),
    path('bar_data/', views.bar_data, name="bar_data"),
    path('sync_ips/', views.sync_ips, name="sync_ips"),
    path('map_data/', views.map_data, name="map_data"),
]
