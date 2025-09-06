from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('meeting/', views.VideoCallView.as_view(), name='meeting'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('join/', views.JoinRoomView.as_view(), name='join_room'),
]
