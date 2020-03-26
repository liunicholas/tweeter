from django.contrib import admin

# Register your models here.
from .models import Post
from .models import MyUser

admin.site.register(Post)
admin.site.register(MyUser)
