from django.contrib import admin
from django.urls import path
from studentorg.views import HomePageView  
from studentorg import views
# 1. Add these two imports


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.HomePageView.as_view(), name="home"),
]

