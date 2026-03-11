from django.contrib import admin
from .models import Task, Category, Profile

# تسجيل Model في لوحة التحكم
admin.site.register(Task)
admin.site.register(Category)
admin.site.register(Profile)
