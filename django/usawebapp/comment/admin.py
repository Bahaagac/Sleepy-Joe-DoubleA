from django.contrib import admin
from .models import Comment
from .models import Review

# Register your models here.

admin.site.register(Comment)
admin.site.register(Review)