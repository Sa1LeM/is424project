from django.urls import path
from . import views

app_name = "appPages"
urlpatterns = [
    path("login", views.login, name="login"),
    path("register",views.register, name="register")
]