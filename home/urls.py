from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.home,name='home'),
    path('register/', views.registerPage,name='registerPage'),
    path('login/', views.loginPage,name='loginPage'),
    path('logout/', views.logoutuser,name='logout'),
]