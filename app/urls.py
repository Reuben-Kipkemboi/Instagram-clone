from django.urls import path,include
from . import views

urlpatterns=[
    path('', views.app_home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('new/post', views.new_post, name='new_post'),
    path('logout/', views.user_logout, name="logout"),
    path('profile/', views.user_profile, name='profile'),
    path('search/', views.search, name='search_results'),
]