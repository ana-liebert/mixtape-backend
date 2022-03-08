from django.db import models
from django.contrib.auth.models import User
import time
from django.contrib.postgres.fields import ArrayField


class Genre(models.Model):
    name = models.CharField(max_length = 150)

    def __str__(self):
        return self.name

SCHEDULE_CHOICES = (
    ("monthly", "Monthly"),
    ("weekly", "Weekly"),
    ("guest", "Guest Spot"),
)

class Host(models.Model):
    name = models.CharField(max_length = 100)
    bio = models.CharField(max_length = 300)
    image = models.CharField(max_length = 200)
    schedule = models.CharField(max_length=50, choices=SCHEDULE_CHOICES)

    def __str__(self):
        return self.name

class Mix(models.Model):
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 200)
    created_at = models.DateTimeField(auto_now_add=True)
    host = models.ForeignKey(Host, on_delete=models.CASCADE, related_name="hosts")
    image = models.CharField(max_length = 200)
    genre = models.ManyToManyField(Genre)
    soundcloudplayer = models.CharField(max_length = 500)
    soundcloudlink = models.CharField(max_length = 300)
    soundclouduser = models.CharField(max_length = 300)
    tracklist = ArrayField(ArrayField(models.CharField(max_length = 600)))
    
    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorites = models.ManyToManyField(Mix, related_name='favorited_by')