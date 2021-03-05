from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('notification/', views.notification, name="Thông Báo"),
    path('Posts/', views.Posts, name="Bài Đăng"),
    path('Profile/', views.Profile, name="Hồ Sơ Cá Nhân"),
]
