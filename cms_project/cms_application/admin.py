from django.contrib import admin

# Register your models here.
from .models import customer, Post, Like

admin.site.register(customer)
admin.site.register(Post)
admin.site.register(Like)