from django.urls import path
from user import views

app_name = 'user'

urlpatterns = [
    path('', views.login, name="login"),
    path('index/', views.index, name="index"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    # path('valid_login/',views.valid_login,name="valid_login"),
    path('user_add/', views.user_add, name="user_add"),
]
