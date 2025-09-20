from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.register, name = 'register'),
    path('login/', views.user_login, name = 'login'),
    path('logout/', views.user_logout, name = 'logout'),
    path('profile/', views.profile, name = 'profile'),
    path('profile/update', views.user_update, name = 'update_profile'),
    path('profile/update/change_pass', views.change_password, name = 'change_pass'),
]