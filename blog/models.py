from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

# class GeneralUser(models.Model):
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=30)
#     nickname = models.CharField(max_length=30, unique=True)
#     phone = models.CharField(max_length=11)
#     gender = models.CharField(max_length=7, choices=GENDER_CHOICES, default='Male')
#     year = models.IntegerField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.email

# class PhamUser(models.Model):
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=30)
#     name = models.CharField(max_length=30)
#     phone = models.CharField(max_length=11)
#     gender = models.CharField(max_length=7, choices=GENDER_CHOICES, default='Male')
#     license_img = models.ImageField(blank=True)
#     workcondition = models.Choices
    
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.email