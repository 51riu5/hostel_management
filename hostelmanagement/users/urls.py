from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.signup, name='signup'),
    path("login/", views.login, name='login'),
    path("profile/", views.profile, name='profile'),
    path("", views.login, name='login'),

]