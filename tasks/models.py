from django.db import models
from django.contrib.auth.models import User

# Model يمثل المهمة (Task)
class Task(models.Model):

    # عنوان المهمة
    title = models.CharField(max_length=200)

    # وصف المهمة
    description = models.TextField(blank=True)

    # حالة المهمة (تمت أم لا)
    completed = models.BooleanField(default=False)

    # تاريخ إنشاء المهمة
    created_at = models.DateTimeField(auto_now_add=True)

    # ربط المهمة بالمستخدم
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # الشكل اللي يظهر في admin panel
    def __str__(self): 
        return self.title
    
  # Model الكاتيجوري
class Category(models.Model):

    # اسم الكاتيجوري
    name = models.CharField(max_length=100)

    # صاحب الكاتيجوري
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
class Profile(models.Model):

    # ربط البروفايل بالمستخدم
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # نبذة عن المستخدم
    bio = models.TextField(blank=True)

    # رقم الهاتف
    phone = models.CharField(max_length=20, blank=True)

    # صورة المستخدم
    image = models.ImageField(upload_to='profiles/', blank=True, null=True)

    def __str__(self):
        return self.user.username
