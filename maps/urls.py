from django.contrib import admin
from django.urls import path, include
from .views import homePageView, uni, signup, delete

urlpatterns = [
    path("", homePageView, name="home"),
    path("signup/", signup, name="signup"),
    path("<int:id>/", uni, name="uni"),
    path("<int:id>/delete/", delete, name="delete"),
    path("accounts/", include("django.contrib.auth.urls")),
]
