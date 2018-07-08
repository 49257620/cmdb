from django.urls import path
from asset import views

app_name = 'asset'

urlpatterns = [
    path('', views.index, name="index"),
    path('list_ajax/', views.list_ajax, name="list_ajax"),
    path('monitor_ajax/', views.monitor_ajax, name="monitor_ajax"),
]
