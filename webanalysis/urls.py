from django.urls import path
from webanalysis import views

app_name = 'webanalysis'

urlpatterns = [
    path('', views.index, name="index"),
    path('upload/', views.upload, name="upload"),
]
