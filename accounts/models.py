from django.db import models

from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='static/profile_images')

