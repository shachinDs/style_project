from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="profile")
    profile_picture = models.FileField()
    bio = models.CharField(max_length=256)
    gender = models.CharField(max_length=10)
    relationship = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.user.username}"



class Location(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="location", primary_key=True)
    longitude = models.FloatField(default=0.0)
    latitude = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.user.username}"





class Friend(models.Model):
    sender = models.TextField(max_length=20)
    receiver = models.TextField(max_length=20)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.sender}"