from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('signup/', views.signupPage, name='signupPage'),
    path('login/', views.loginPage, name='loginPage'),
    path('logout/', views.logoutUser, name='logoutPage'),
    path('all/', views.allPage, name='allPage'),
    path('top/', views.topPage, name='topPage'),
    path('all/<slug:slug>/', views.allPage, name='filterPage'),
    path('movie/<int:pk>/', views.moviePage, name='moviePage'),

]
