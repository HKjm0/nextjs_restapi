from django.contrib import admin

# Register your models here.
from .models import Task, Post

admin.site.register(Post)
admin.site.register(Task)