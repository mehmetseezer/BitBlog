from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from home import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),  # new
    path("accounts/", include("django.contrib.auth.urls")),
    path("", views.home, name="home"),
    path("add_blog/", views.add_blog, name="add_blog"),
    path('see_blogs/', views.see_blog, name='see_blog')
]