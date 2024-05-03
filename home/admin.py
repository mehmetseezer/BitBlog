from django.contrib import admin

# Register your models here.
from .models import BlogModel

# admin sayfasında görüntülenecek Modeller
admin.site.register(BlogModel)