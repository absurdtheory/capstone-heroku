# Registered Models in admin.py
from django.contrib import admin
from backend.posts.models import Comment, Post

admin.site.register(Comment)
admin.site.register(Post)
