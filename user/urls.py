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
    path('user_update/', views.user_update, name="user_update"),
    path('user_delete/', views.user_delete, name="user_delete"),
    path('user_chpwd/', views.user_chpwd, name="user_chpwd"),
]
