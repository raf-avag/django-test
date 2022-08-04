from django.contrib import admin
from django.urls import path, include
from .views import (
    homePageView,
    uni,
    signup,
    delete,
    UniList,
    UniCreate,
    UniDetail,
    UniUpdate,
    UniDelete,
)

urlpatterns = [
    path("", homePageView, name="home"),
    path("signup/", signup, name="signup"),
    path("<int:id>/", uni, name="uni"),
    path("uni", UniList.as_view(), name="uni"),
    path("uni/<int:pk>/", UniDetail.as_view(), name="uni-detail"),
    path("uni-create/", UniCreate.as_view(), name="uni-create"),
    path("uni-update/<int:pk>/", UniUpdate.as_view(), name="uni-update"),
    path("uni-delete/<int:pk>/", UniDelete.as_view(), name="uni-delete"),
    path("<int:id>/delete/", delete, name="delete"),
    path("accounts/", include("django.contrib.auth.urls")),
]
