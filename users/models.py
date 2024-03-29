from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255, null=False)
    email = models.EmailField(max_length=255, null=False)
    phone_number = models.CharField(max_length=255, null=False)
    address = models.CharField(max_length=255, null=False)
    ssid = models.CharField(max_length=255, null=False)
    is_active = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class UserProfile(models.Model):
    DEFAULT_PROFILE_PIC_URL = "https://im.rediff.com/money/2011/apr/20vodafone1.jpg"
    profile_pic_url =  models.CharField(max_length=255, default=DEFAULT_PROFILE_PIC_URL)
    bio = models.CharField(max_length=255, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
