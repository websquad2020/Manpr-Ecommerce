from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    url(r"^login/$", views.login_view, name = "login"),
    url(r"^register/$", views.register_view, name = "register"),
    #path('login/', views.home, name="home"),
    #path('signup/', views.signup, name="signup"),
    #path('login/',views.login, name="login"),
]