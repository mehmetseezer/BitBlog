from django.urls import path
from .views import *

# routes
urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('add_blog/', add_blog, name="add_blog"),
    path('see_blog/', see_blog, name='see_blog'),
    path('register/', register, name='register_view'),
    path('logout/', logout, name="logout"),
    path('blog_detail/<slug>', blog_detail, name='blog_detail')
]